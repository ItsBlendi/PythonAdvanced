from fontTools.misc.bezierTools import printSegments

contact_info = {
    "Blend": "049-162-251",
    "Aldini": "049-911-869"
}

blend_phone = contact_info ["Blend"]
print(blend_phone)

contact_info["Blend"] = "044-162-251"
print(contact_info)

contact_info["Florjoni"] = "049-835-766"
print(contact_info)

del contact_info ["Aldini"]
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)

contact_information = {
    "Alice" : {
        "phone_number" : "123-456",
        "email" : "alice@gmail,com",
        "birthday": "20/12/2008"
    } ,

    "Bob":{
        "phone_number" : "123-555",
        "email" : "bob@gmail,com",
        "birthday": "27/12/2008"
    }
}
print(contact_information)
print(contact_information["Bob"])
