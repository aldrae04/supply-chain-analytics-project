from pathlib import Path
import duckdb

def main() -> None:
        script_dir = Path(__file__).resolve().parent
        db_path = (script_dir /".."/ "1_data_source" / "supply_chain_analytics.duckdb").resolve()
        con = duckdb.connect(str(db_path))

        con.execute("""
        CREATE OR REPLACE TABLE bronze__product_master__lite AS
        SELECT * FROM raw__product_master__lite;
        """)

        con.close()
        print("DONE: bronze__product_master__lite")

if __name__ == "__main__":
    main()