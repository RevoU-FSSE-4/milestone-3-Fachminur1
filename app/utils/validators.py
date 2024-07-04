from flask import jsonify

def validate_account_data(data):
    """
    Validates the account data for required fields and types.
    """
    required_fields = ['account_type', 'account_number', 'balance']
    for field in required_fields:
        if field not in data:
            return jsonify({"msg": f"Missing {field}"}), 400
        if field == 'balance' and not isinstance(data[field], (int, float)):
            return jsonify({"msg": f"Invalid type for {field}"}), 400
    return None

def validate_transaction_data(data):
    """
    Validates the transaction data for required fields and types.
    """
    required_fields = ['from_account_id', 'amount', 'transaction_type']
    for field in required_fields:
        if field not in data:
            return jsonify({"msg": f"Missing {field}"}), 400
        if field == 'amount' and not isinstance(data[field], (int, float)):
            return jsonify({"msg": f"Invalid type for {field}"}), 400
    return None