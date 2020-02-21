#---Dictionary Basics-----------
my_dict={"key1":"value1","key2":"value2"}
print(my_dict)
print(my_dict["key1"])

#Real life scenario for dictionary
product_price={"Apples":2.99,"Oranges":50.45,"Milk":80.90}
price_pu=product_price[str(input("Product: "))]
order_qty=int(input("Number of units: "))
#print("The price of R " + str(product_price[str(input("Product: "))]))

print("The order of "+str(order_qty) +" will be R" +str((price_pu * order_qty)))

#complex dictionaries
cd={"k1":123,"k2":[0,1,2,3],"k3":{"insideKey":100}}
#Printing the element in the k3 of cd
print(str(cd["k3"]["insideKey"]))