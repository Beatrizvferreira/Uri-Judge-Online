SELECT products.NAME,
       providers.NAME,
       categories.NAME
FROM products 
LEFT join providers ON ( products.id_providers = providers.ID)
LEFT join categories ON ( products.id_categories = categories.ID)
WHERE providers.NAME = 'Sansul SA' AND categories.NAME = 'Imported'