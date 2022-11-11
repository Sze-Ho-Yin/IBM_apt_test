SELECT owner_id, owner_name, COUNT()
FROM owner, article, category_aricle_mapping, category
WHERE owner.owner_id==article.owner_id AND category_aricle_mapping.article_id==article.article_id 
AND category.category_id == category_aricle_mapping.category_id
GROUP_BY owner_id
ORDER_BY