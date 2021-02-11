#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:50:54 2021
@author: pradeepa
app= express()
app.get('',())
app.post('',())
"""

import json
from flask import Flask,jsonify,request,Response,make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:admin@localhost:3306/devops'

db = SQLAlchemy(app)


class Product(db.Model):
    __tablename__="pyproducts"
    productId = db.Column(db.Integer,primary_key=True)
    productName = db.Column(db.String(40))
    description = db.Column(db.String(60))
    productCode = db.Column(db.String(40))
    price = db.Column(db.Float)
    starRating = db.Column(db.Float)
    imageUrl = db.Column(db.String(40))
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    def __init__(self,productName,description,productCode,price,starRating,imageUrl):
        self.productName = productName
        self.description = description
        self.productCode = productCode
        self.price = price
        self.starRating = starRating
        self.imageUrl = imageUrl
    def  __repr__(self):
        return "% self.productId"
 
db.create_all()    

class ProductSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Product
        sqla_session = db.session
    productId = fields.Number(dump_only=True)
    productName = fields.String(required=True)
    description = fields.String(required=True)
    productCode = fields.String(required=True)
    price = fields.Number(required=True)
    starRating = fields.Number(required=True)
    imageUrl = fields.String(required=True)

#http://localhost:4002/products
@app.route('/products',methods=['POST'])
def createProduct():
    data = request.get_json()
    product_schema = ProductSchema()
    product = product_schema.load(data)
    result = product_schema.dump(product.create())
    return make_response(jsonify({"product":result}),201)

@app.route('/products',methods=['GET'])
def getAllProducts():
    get_products=Product.query.all()
    productSchema=ProductSchema(many=True)
    products=productSchema.dump(get_products)
    return make_response(jsonify({"products":products}),200)

@app.route('/products/<int:productId>',methods=['GET'])
def getProductById(productId):
    get_product=Product.query.get(productId)
    productSchema=ProductSchema()
    product=productSchema.dump(get_product)
    return make_response(jsonify({"product":product}),200)

@app.route('/products/<int:productId>',methods=['DELETE'])
def deleteProductById(productId):
    get_product=Product.query.get(productId)
  
    db.session.delete(get_product)
    db.session.commit()
    return make_response(jsonify({"result":"product deleted"}),204)  

    
@app.route('/products/<int:productId>',methods=['PUT'])
def updateProduct(productId):
    data = request.get_json()
    get_product=Product.query.get(productId)
    if data.get('price'):
        get_product.price = data['price']
    db.session.add(get_product)
    db.session.commit()
    
    
    product_schema = ProductSchema(only=['productId','price'])
   
    result = product_schema.dump(get_product)
    return make_response(jsonify({"product":result}),200)


@app.route('/products/find/<productName>',methods=['GET'])
def getProductsByName(productName):
    get_products=Product.query.filter_by(productName=productName)
    productSchema=ProductSchema(many=True)
    products=productSchema.dump(get_products)
    return make_response(jsonify({"product":products}),200)
    


app.run(port=4002)


# Grade Sorter App

# What is your first grade (0-100):
    
# What is your second grade (0-100):
    
# What is your third grade (0-100):

# What is your fourth grade (0-100):    
            
    # grades are [88,95,56,71]
    
    # Find The highes grade and display
    
    
# Voter Registration App

# please enter u r name : 
    
# please enter u r age: 18

# List Political Parties To Join

# BJP
# Congress
# NCP
# SP
#  Which party u would like to join BJP
# Congratulation u r membership is accepted

# No of Memberships each party has got

# Enter The Party Name
# Congress
# No Of Memberships





    

    
    
