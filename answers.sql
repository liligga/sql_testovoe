-- первое задание
SELECT g.name, SUM(qty) as product_amount from "actionTable" as a
JOIN "goodsList" as g ON g.id=a.good_id
JOIN "storeList" as s ON a.store_from_id=s.id
WHERE s.name = "Магазин 1" AND (a.action_date BETWEEN '2023-02-10' AND '2023-05-10') -- название склада и период дат 
GROUP BY good_id ORDER BY g.name;

-- второе задание
SELECT b.name, SUM(qty) as product_amount from "actionTable" as a
JOIN "goodsList" as g ON g.id=a.good_id
JOIN "storeList" as s ON a.store_to_id=s.id
LEFT JOIN "brandList" as b ON g.brand_id=b.id
WHERE s.name = "Магазин 1" AND (a.action_date BETWEEN '2023-02-10' AND '2023-05-10')
GROUP BY brand_id ORDER BY b.name;

-- третье задание
SELECT g.name as good_name,
    COALESCE(SUM(
       CASE 
            WHEN a.store_to_id = s.id THEN a.qty
            WHEN a.store_from_id = s.id THEN -a.qty
            ELSE 0
        END
    ), 0) as total_product_amount
FROM goodsList g
CROSS JOIN storeList s
LEFT JOIN actionTable a ON g.id = a.good_id 
    AND a.action_date <= '2024-01-18'
    AND (a.store_to_id = s.id OR a.store_from_id = s.id)
WHERE s.name = 'Магазин 1'
GROUP BY g.name, g.id 
ORDER BY g.name;

-- четвертое задание
SELECT g.name, SUM(qty) as product_amount from "actionTable" as a
JOIN "goodsList" as g ON g.id=a.good_id
JOIN "storeList" as s ON a.store_to_id=s.id
JOIN contractorList as c ON a.contractor_from_id=c.id
WHERE s.name = "Магазин 1" AND c.name = 'Поставщик 1' AND (a.action_date BETWEEN '2023-02-10' AND '2023-05-10') -- название склада, поставщика и период дат 
GROUP BY g.id ORDER BY g.name;

-- пятое задание
SELECT c.name, SUM(qty) as product_amount from "actionTable" as a
JOIN "goodsList" as g ON g.id=a.good_id
JOIN contractorList as c ON a.contractor_from_id=c.id -- JOIN с storeList не нужен, ибо не должно быть записей с contractor_from_id и contractor_to_id или contractor_from_id и store_from_id не NULL 
WHERE g.name='Удобные кроссы' AND (a.action_date BETWEEN '2023-02-10' AND '2023-05-10')
GROUP BY c.id ORDER BY sum_product;

-- шестое задание
SELECT g.name, SUM(qty) AS product_amount from "actionTable" as a
JOIN "goodsList" as g ON g.id=a.good_id
JOIN "storeList" as s ON a.store_to_id=s.id
WHERE s.name = "Магазин 1" AND a.store_from_id IS NOT NULL AND (a.action_date BETWEEN '2023-02-10' AND '2023-05-10') -- название склада и период дат 
GROUP BY g.id ORDER BY g.name;


-- третье задание без группирования, где я хотел подробно увидеть "перетикание" товаров в склад и из
SELECT g.name as good_name,
       CASE 
            WHEN a.store_to_id = s.id THEN a.qty
            WHEN a.store_from_id = s.id THEN -a.qty
            ELSE 0
        END as amount,
a.store_to_id, a.store_from_id, a.contractor_from_id, a.contractor_to_id, a.action_date
FROM goodsList g
CROSS JOIN storeList s
LEFT JOIN actionTable a ON g.id = a.good_id 
    AND a.action_date <= '2024-01-18'
    AND (a.store_to_id = s.id OR a.store_from_id = s.id)
WHERE s.name = 'Магазин 1'
ORDER BY g.name;