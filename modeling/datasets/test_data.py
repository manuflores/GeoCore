import os

from modeling.datasets.base import BaseFeatures
from modeling.datasets.build import TEST_REGISTRY


@TEST_REGISTRY.register()
class IngeniousHotSprings(BaseFeatures):
    table_name = "ING_HOTSPRINGS"
    index_column = "H3_BLOCKS"
    run_checks = False
    sql_code = f"""
      with hot_springs as (
        select
              H3_LATLNG_TO_CELL_STRING( LATDEGREE, LONGDEGREE, 8) as H3_BLOCKS
            , 1 as LABEL
            , 1 as WEIGHT
        from ZANSKAR_SNOWFLAKE_MARKETPLACE.INGENIOUS.INGENIOUS_SPRING_TEMPERATURE
        where MEASUREDTEMP_C >= 40
        GROUP BY H3_BLOCKS
      )
      SELECT
      distinct
        H3_BLOCKS
        , LABEL
        , WEIGHT
        , 'KNOWN' as TYPE
      FROM
        hot_springs
        where H3_BLOCKS is not null
    """


@TEST_REGISTRY.register()
class Fishing(BaseFeatures):
    table_name = "TRAWLERS_FEAT_ENG"
    index_column = "mmsi"
    sql_code = """
    SELECT 
    "is_fishing" 
    FROM FISHING.CLASSIFIER_SCHEMA.TRAWLERS_FEAT_ENG
    """