from pathlib import Path
import duckdb, pandas as pd

def main() -> None:
        script_dir = Path(__file__).resolve().parent
        db_path = (script_dir /".."/ "1_data_source" / "supply_chain_analytics.duckdb").resolve()
        xlsx_path = (script_dir /".."/ "1_data_source" / "raw__location_master__lite.xlsx").resolve()

        print("Loading Excel from: ", xlsx_path)
        con = duckdb.connect(str(db_path))
        df = pd.read_excel(xlsx_path)
        con.register("tmp__location_master__lite", df)

        con.execute("""
        CREATE OR REPLACE TABLE bronze__location_master__lite AS
        SELECT
                location_id,
                location_name,
                location_type,
                region
        FROM tmp__location_master__lite;
        """)

        con.close()
        print("DONE: Created bronze__location_master__lite")

if __name__ == "__main__":
    main()