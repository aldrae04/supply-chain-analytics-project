from pathlib import Path
import duckdb

def main() -> None:
        script_dir = Path(__file__).resolve().parent
        db_path = (script_dir /".."/ "1_data_source" / "supply_chain_analytics.duckdb").resolve()
        con = duckdb.connect(str(db_path))

        con.execute("""
            CREATE OR REPLACE TABLE gold__dim_product AS
            SELECT
                sku             AS ProductSKU,
                product_name    AS ProductName,
                category        AS ProductCategory,
                brand           AS Brand,
                unit_cost       AS UnitCost
            FROM silver__product_master__lite;
            
        """)

        con.close()
        print("DONE: Created gold__dim_product")

if __name__ == "__main__":
    main()