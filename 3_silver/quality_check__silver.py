from pathlib import Path
import duckdb

def main() -> None:
        script_dir = Path(__file__).resolve().parent
        db_path = (script_dir /".."/ "1_data_source" / "supply_chain_analytics.duckdb").resolve()

        with duckdb.connect(str(db_path)) as con:

            # 1. SKU Uniqueness Check
            print("1. SKU Uniqueness Check")
            con.sql("""
                SELECT sku, COUNT(*) AS cnt 
                FROM silver__product_master__lite 
                GROUP BY 1 
                HAVING COUNT(*) > 1;
            """).show()

            # 2. Location uniqueness
            print("2. Location Uniqueness Check")
            con.sql("""
                SELECT location_id, COUNT(*) AS cnt 
                FROM silver__location_master__lite 
                GROUP BY 1 
                HAVING COUNT(*) > 1;
            """).show()

            # 3. Fact SKUs not in product dimension
            print("3. Fact SKUs not in product dimension")
            con.sql("""
                SELECT DISTINCT s.sku 
                FROM silver__sales_transactions__lite s 
                LEFT JOIN silver__product_master__lite p ON s.sku = p.sku 
                WHERE p.sku IS NULL 
                LIMIT 100;
            """).show()

            # 4. Date null rate (sales)
            print("4. Date null rate (sales)")
            con.sql("""
                SELECT COUNT(*) AS total_rows, 
                SUM(CASE WHEN transaction_date IS NULL THEN 1 ELSE 0 END) AS null_dates 
                FROM silver__sales_transactions__lite;
            """).show()

            # 5. Movement type validity
            print("5. Movement type validity")
            con.sql("""
                SELECT movement_type, COUNT(*) AS cnt 
                FROM silver__inventory_movements__lite 
                GROUP BY 1 
                ORDER BY cnt DESC;
            """).show()

        print("DONE: Silver Layer Quality Checks Display Completed")

if __name__ == "__main__":
    main()