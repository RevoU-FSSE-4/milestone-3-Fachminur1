from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Account
from app.extensions import db

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/', methods=['GET'])
@jwt_required()
def get_accounts():
    user_id = get_jwt_identity()
    accounts = Account.query.filter_by(user_id=user_id).all()
    return jsonify([account.to_dict() for account in accounts]), 200

@accounts_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_account(id):
    account = Account.query.get_or_404(id)
    return jsonify(account.to_dict()), 200

@accounts_bp.route('/', methods=['POST'])
@jwt_required()
def create_account():
    user_id = get_jwt_identity()
    account_type = request.form.get('account_type')
    account_number = request.form.get('account_number')
    balance = float(request.form.get('balance', 0.00))

    if not account_type or not account_number:
        return jsonify({'error': 'Missing required fields'}), 400

    existing_account = Account.query.filter_by(account_number=account_number).first()
    if existing_account:
        return jsonify({'error': 'Account number already exists'}), 400

    account = Account(
        user_id=user_id,
        account_type=account_type,
        account_number=account_number,
        balance=balance
    )
    
    db.session.add(account)
    db.session.commit()
    
    return jsonify(account.to_dict()), 201

@accounts_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_account(id):
    account = Account.query.get_or_404(id)

    account_type = request.form.get('account_type')
    balance = float(request.form.get('balance'))

    account.account_type = account_type
    account.balance = balance

    db.session.commit()
    
    return jsonify(account.to_dict()), 200

@accounts_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_account(id):
    account = Account.query.get_or_404(id)
    db.session.delete(account)
    db.session.commit()
    return '', 204