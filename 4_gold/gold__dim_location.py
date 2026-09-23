from pathlib import Path
import duckdb

def main() -> None:
        script_dir = Path(__file__).resolve().parent
        db_path = (script_dir /".."/ "1_data_source" / "supply_chain_analytics.duckdb").resolve()
        con = duckdb.connect(str(db_path))

        con.execute("""
            CREATE OR REPLACE TABLE gold__dim_location AS
            SELECT
                location_id     AS LocationID,
                location_name   AS LocationName,
                location_type   AS LocationType,
                region          AS Region
            FROM silver__location_master__lite;
            
        """)

        con.close()
        print("DONE: Created gold__dim_location")

if __name__ == "__main__":
    main()