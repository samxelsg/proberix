import sqlite3
import pandas as pd
import os

file_1 = r"D:\School\Programming\Python\df_promotion_payment_transaction_and_request.csv"
file_2 = r"D:\School\Programming\Python\cleaned_dim_paper_company.csv"
file_3 = r"D:\School\Programming\Python\df_feature_engineering_promotion_payment_transaction_and_request.csv"

# koneksi sql
conn = sqlite3.connect("data_integration.db")

# baca file
df_transactions = pd.read_csv(file_1)
df_company = pd.read_csv(file_2)
df_feature_engineered = pd.read_csv(file_3)

# load data ke sql table
df_transactions.to_sql("promotion_transactions", conn, index=False, if_exists="replace")
df_company.to_sql("companies", conn, index=False, if_exists="replace")
df_feature_engineered.to_sql("feature_engineered_transactions", conn, index=False, if_exists="replace")

# query
query = """
SELECT 
    -- Fields from companies
    c.company_id,
    c.company_kyc_status_name,
    c.company_kyb_status_name,
    c.company_type_group,
    c.company_phone_verified_flag,
    c.company_email_verified_flag,
    c.user_fraud_flag,
    c.testing_account_flag,
    c.blacklist_account_flag,
    c.package_active_name,
    c.company_registered_datetime,

    -- Fields from promotion_transactions
    t.dpt_id AS transaction_id,
    t.buyer_id,
    t.seller_id,
    t.transaction_amount,
    t.payment_method_name,
    t.payment_provider_name,
    t.transaction_created_datetime,
    t.transaction_updated_datetime,
    t.total_fee_amount,
    t.document_type_name,
    t.dpt_promotion_id,
    t.promotion_code,
    t.promotion_name,
    t.transaction_promo_cashback_amount,

    -- Fields from feature_engineered_transactions
    f.interaction_count,
    f.z_score,
    f.is_anomaly,
    f.time_diff,
    f.time_diff_mean,
    f.time_diff_std,
    f.is_burst,
    f.is_gaps,
    f.is_timing_anomaly,
    f.usage_count,
    f.cashback_total,
    f.is_promotion_code_exploited

FROM 
    promotion_transactions AS t
JOIN 
    companies AS c 
ON 
    t.seller_id = c.company_id
JOIN 
    feature_engineered_transactions AS f 
ON 
    t.dpt_id = f.dpt_id;
"""
# cwd
current_directory = os.getcwd()
output_folder = os.path.join(current_directory, "output_results")

# create folder output data kalo blom ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# part partnyah
output_base_path = os.path.join(output_folder, "integrated_results_part_")

# pembagian chunk biar ga kegedean filenya
chunk_size = 1000000 

for i, chunk in enumerate(pd.read_sql_query(query, conn, chunksize=chunk_size)):
    output_path = f"{output_base_path}{i+1}.csv"
    chunk.to_csv(output_path, index=False)
    print(f"bagian {i+1} dari hasil disimpan di {output_path}")

# koneksi
conn.close()
