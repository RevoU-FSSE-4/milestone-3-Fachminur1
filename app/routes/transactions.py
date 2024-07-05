from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Transaction, Account
from app.extensions import db

transactions_bp = Blueprint('transactions',__name__,url_prefix = "/transactions")

@transactions_bp.route('/', methods=['GET'])
@jwt_required()
def get_transactions():
    user_id = get_jwt_identity()
    transactions = Transaction.query.join(Account, Transaction.from_account_id == Account.id).filter(Account.user_id == user_id).all()
    return jsonify([transaction.to_dict() for transaction in transactions]), 200

@transactions_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    return jsonify(transaction.to_dict()), 200

@transactions_bp.route('/', methods=['POST'])
@jwt_required()
def create_transaction():
    user_id = get_jwt_identity()
    
    data = request.json
    
    from_account_id = data.get('from_account_id')
    to_account_id = data.get('to_account_id')
    amount = data.get('amount')
    transaction_type = data.get('transaction_type')
    description = data.get('description')

    if not from_account_id or not amount or not transaction_type:
        return jsonify({"error": "Missing required fields"}), 400
    
    try:
        amount = float(amount)
    except ValueError:
        return jsonify({"error": "Invalid amount"}), 400

    from_account = Account.query.filter_by(id=from_account_id, user_id=user_id).first_or_404()
    to_account = Account.query.filter_by(id=to_account_id).first() if to_account_id else None

    transaction = Transaction(
        from_account_id=from_account.id,
        to_account_id=to_account.id if to_account else None,
        amount=amount,
        transaction_type=transaction_type,
        description=description
    )
    
    db.session.add(transaction)
    db.session.commit()

    return jsonify({"message": "Transaction created successfully"}), 201