SELECT products.NAME,
       providers.NAME,
       products.PRICE
       
FROM products 
LEFT join providers ON ( products.id_providers = providers.ID)
LEFT join categories ON ( products.id_categories = categories.ID)
WHERE categories.NAME = 'Super Luxury' and products.PRICE > 1000