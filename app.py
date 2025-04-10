from flask import Flask, request, jsonify
import pandas as pd
import ibm_boto3
from ibm_botocore.client import Config
import os

app = Flask(__name__)


@app.route('/get-manager', methods=['POST'])
def get_manager():
    try:
        data = request.get_json()
        cliente = data.get('cliente', '').strip().upper()

        cos_api_key = os.getenv('COS_API_KEY')
        cos_instance_id = os.getenv('COS_INSTANCE_ID')
        bucket_name = os.getenv('BUCKET_NAME')
        object_name = os.getenv('OBJECT_NAME')

        cos = ibm_boto3.client("s3",
                               ibm_api_key_id=cos_api_key,
                               ibm_service_instance_id=cos_instance_id,
                               config=Config(signature_version="oauth"),
                               endpoint_url="https://s3.us-south.cloud-object-storage.appdomain.cloud"
                               )

        response = cos.get_object(Bucket=bucket_name, Key=object_name)
        df = pd.read_csv(response['Body'])

        df['Full Customer Name'] = df['Full Customer Name'].astype(
            str).str.upper().str.strip()

        result = df[df['Full Customer Name'] == cliente]

        if result.empty:
            return jsonify({"erro": "Cliente não encontrado."}), 404

        gerente = result['NA EOL Account Manager'].values[0]
        return jsonify({"account_manager": gerente})

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
