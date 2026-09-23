from pathlib import Path
import duckdb

def main() -> None:
        script_dir = Path(__file__).resolve().parent
        db_path = (script_dir /".."/ "1_data_source" / "supply_chain_analytics.duckdb").resolve()
        con = duckdb.connect(str(db_path))

        con.execute("""
            CREATE OR REPLACE TABLE gold__fact_sales AS
            SELECT
                transaction_id      AS SalesTransactionID,
                transaction_date    AS SalesDate,
                location_id         AS LocationID,
                sku                 AS ProductSKU,
                qty                 AS Quantity,
                unit_price          AS UnitPrice
            FROM silver__sales_transactions__lite
            
        """)

        con.close()
        print("DONE: Created gold__fact_sales")

if __name__ == "__main__":
    main()