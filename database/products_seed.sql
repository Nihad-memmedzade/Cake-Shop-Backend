-- Generated from cake-house-backend/app/data/products.py
-- Images are stored as JSONB URL arrays, exactly like the backend product data.

CREATE TABLE IF NOT EXISTS products (
  id INTEGER PRIMARY KEY,
  title VARCHAR(180) NOT NULL,
  quantity INTEGER NOT NULL DEFAULT 1,
  category VARCHAR(100) NOT NULL,
  flavor VARCHAR(100) NOT NULL,
  tags JSONB NOT NULL DEFAULT '[]'::jsonb,
  price DOUBLE PRECISION NOT NULL,
  "discountedPrice" DOUBLE PRECISION NOT NULL DEFAULT 0,
  rating DOUBLE PRECISION NOT NULL DEFAULT 0,
  images JSONB NOT NULL DEFAULT '[]'::jsonb,
  brand VARCHAR(120) NOT NULL,
  sizes JSONB NOT NULL DEFAULT '[]'::jsonb,
  description TEXT NOT NULL,
  "isNewArrival" BOOLEAN NOT NULL DEFAULT FALSE,
  "isTopRated" BOOLEAN NOT NULL DEFAULT FALSE,
  "isBestSeller" BOOLEAN NOT NULL DEFAULT FALSE,
  "isLimitedEdition" BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE INDEX IF NOT EXISTS ix_products_category ON products (category);
CREATE INDEX IF NOT EXISTS ix_products_flavor ON products (flavor);
CREATE INDEX IF NOT EXISTS ix_products_is_new_arrival ON products ("isNewArrival");
CREATE INDEX IF NOT EXISTS ix_products_is_top_rated ON products ("isTopRated");
CREATE INDEX IF NOT EXISTS ix_products_is_best_seller ON products ("isBestSeller");
CREATE INDEX IF NOT EXISTS ix_products_is_limited_edition ON products ("isLimitedEdition");

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (1, 'Chocolate Dream Cake', 1, 'Celebration Cake', 'Chocolate', '["Nut Free"]'::jsonb, 45, 39, 4.8, '["https://images.unsplash.com/photo-1606313564200-e75d5e30476c", "https://images.unsplash.com/photo-1578985545062-69928b1d9587"]'::jsonb, 'Cake House', '[{"id": 2, "label": "Medium"}, {"id": 3, "label": "Large"}]'::jsonb, 'Rich chocolate cake with creamy frosting.', FALSE, FALSE, TRUE, TRUE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (2, 'Strawberry Cream Cake', 1, 'Fruit Cake', 'Strawberry', '["Low Sugar", "Nut Free"]'::jsonb, 50, 44, 4.7, '["https://images.unsplash.com/photo-1565958011703-44f9829ba187"]'::jsonb, 'Cake House', '[{"id": 1, "label": "Small"}, {"id": 2, "label": "Medium"}]'::jsonb, 'Soft strawberry cream cake.', FALSE, FALSE, FALSE, FALSE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (3, 'Red Velvet Cake', 1, 'Classic Cake', 'Red Velvet', '["Dairy Free"]'::jsonb, 55, 48, 4.9, '["https://images.unsplash.com/photo-1586788680434-30d324b2d46f"]'::jsonb, 'Cake House', '[{"id": 2, "label": "Medium"}, {"id": 3, "label": "Large"}]'::jsonb, 'Classic red velvet cake.', FALSE, TRUE, TRUE, TRUE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (4, 'Vanilla Birthday Cake', 1, 'Birthday Cake', 'Vanilla', '["Nut Free", "Low Sugar"]'::jsonb, 40, 35, 4.6, '["https://images.unsplash.com/photo-1551024601-bec78aea704b"]'::jsonb, 'Cake House', '[{"id": 2, "label": "Medium"}, {"id": 3, "label": "Large"}]'::jsonb, 'Perfect birthday vanilla cake.', FALSE, FALSE, FALSE, FALSE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (5, 'Caramel Cheesecake', 1, 'Cheesecake', 'Caramel', '["Gluten Free"]'::jsonb, 60, 52, 4.9, '["https://images.unsplash.com/photo-1533134242443-d4fd215305ad"]'::jsonb, 'Cake House', '[{"id": 1, "label": "Small"}, {"id": 2, "label": "Medium"}]'::jsonb, 'Creamy caramel cheesecake.', FALSE, TRUE, TRUE, TRUE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (6, 'Blueberry Delight Cake', 1, 'Fruit Cake', 'Blueberry', '["Vegan", "Low Sugar"]'::jsonb, 48, 42, 4.5, '["https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62"]'::jsonb, 'Cake House', '[{"id": 1, "label": "Small"}, {"id": 2, "label": "Medium"}]'::jsonb, 'Fresh blueberry cake.', FALSE, FALSE, FALSE, FALSE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (7, 'Oreo Crunch Cake', 1, 'Celebration Cake', 'Oreo', '["Nut Free"]'::jsonb, 58, 49, 4.8, '["https://images.unsplash.com/photo-1464349095431-e9a21285b5f3"]'::jsonb, 'Cake House', '[{"id": 2, "label": "Medium"}, {"id": 3, "label": "Large"}]'::jsonb, 'Oreo layered cake.', TRUE, FALSE, TRUE, TRUE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (8, 'Lemon Fresh Cake', 1, 'Fresh Cake', 'Lemon', '["Vegan", "Dairy Free", "Low Sugar"]'::jsonb, 43, 0, 4.4, '["https://images.unsplash.com/photo-1576618148400-f54bed99fcfd"]'::jsonb, 'Cake House', '[{"id": 1, "label": "Small"}]'::jsonb, 'Light lemon cake.', TRUE, FALSE, FALSE, FALSE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (9, 'Black Forest Cake', 1, 'Classic Cake', 'Cherry Chocolate', '["Nut Free"]'::jsonb, 62, 54, 4.9, '["https://images.unsplash.com/photo-1563729784474-d77dbb933a9e"]'::jsonb, 'Cake House', '[{"id": 3, "label": "Large"}]'::jsonb, 'Classic black forest cake.', TRUE, TRUE, TRUE, TRUE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (10, 'Pistachio Honey Cake', 1, 'Premium Cake', 'Pistachio', '["Gluten Free"]'::jsonb, 68, 0, 4.8, '["https://images.unsplash.com/photo-1558301211-0d8c8ddee6ec"]'::jsonb, 'Cake House', '[{"id": 2, "label": "Medium"}, {"id": 3, "label": "Large"}]'::jsonb, 'Premium pistachio cake.', TRUE, FALSE, FALSE, TRUE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (11, 'Chocolate Dream Cake', 1, 'Celebration Cake', 'Chocolate', '["Nut Free"]'::jsonb, 45, 39, 4.8, '["https://images.unsplash.com/photo-1606313564200-e75d5e30476c", "https://images.unsplash.com/photo-1578985545062-69928b1d9587"]'::jsonb, 'Cake House', '[{"id": 2, "label": "Medium"}, {"id": 3, "label": "Large"}]'::jsonb, 'Rich chocolate cake with creamy frosting.', FALSE, FALSE, TRUE, TRUE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (12, 'Strawberry Cream Cake', 1, 'Fruit Cake', 'Strawberry', '["Low Sugar", "Nut Free"]'::jsonb, 50, 44, 4.7, '["https://images.unsplash.com/photo-1565958011703-44f9829ba187"]'::jsonb, 'Cake House', '[{"id": 1, "label": "Small"}, {"id": 2, "label": "Medium"}]'::jsonb, 'Soft strawberry cream cake.', FALSE, FALSE, FALSE, FALSE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (13, 'Red Velvet Cake', 1, 'Classic Cake', 'Red Velvet', '["Dairy Free"]'::jsonb, 55, 48, 4.9, '["https://images.unsplash.com/photo-1586788680434-30d324b2d46f"]'::jsonb, 'Cake House', '[{"id": 2, "label": "Medium"}, {"id": 3, "label": "Large"}]'::jsonb, 'Classic red velvet cake.', FALSE, TRUE, TRUE, TRUE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (14, 'Chocolate Dream Cake', 1, 'Celebration Cake', 'Chocolate', '["Nut Free"]'::jsonb, 45, 39, 4.8, '["https://images.unsplash.com/photo-1606313564200-e75d5e30476c", "https://images.unsplash.com/photo-1578985545062-69928b1d9587"]'::jsonb, 'Cake House', '[{"id": 2, "label": "Medium"}, {"id": 3, "label": "Large"}]'::jsonb, 'Rich chocolate cake with creamy frosting.', FALSE, FALSE, TRUE, TRUE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (15, 'Strawberry Cream Cake', 1, 'Fruit Cake', 'Strawberry', '["Low Sugar", "Nut Free"]'::jsonb, 50, 44, 4.7, '["https://images.unsplash.com/photo-1565958011703-44f9829ba187"]'::jsonb, 'Cake House', '[{"id": 1, "label": "Small"}, {"id": 2, "label": "Medium"}]'::jsonb, 'Soft strawberry cream cake.', FALSE, FALSE, FALSE, FALSE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";

INSERT INTO products (id, title, quantity, category, flavor, tags, price, "discountedPrice", rating, images, brand, sizes, description, "isNewArrival", "isTopRated", "isBestSeller", "isLimitedEdition")
VALUES (16, 'Red Velvet Cake', 1, 'Classic Cake', 'Red Velvet', '["Dairy Free"]'::jsonb, 55, 48, 4.9, '["https://images.unsplash.com/photo-1586788680434-30d324b2d46f"]'::jsonb, 'Cake House', '[{"id": 2, "label": "Medium"}, {"id": 3, "label": "Large"}]'::jsonb, 'Classic red velvet cake.', FALSE, TRUE, TRUE, TRUE)
ON CONFLICT (id) DO UPDATE SET
  title = EXCLUDED.title,
  quantity = EXCLUDED.quantity,
  category = EXCLUDED.category,
  flavor = EXCLUDED.flavor,
  tags = EXCLUDED.tags,
  price = EXCLUDED.price,
  "discountedPrice" = EXCLUDED."discountedPrice",
  rating = EXCLUDED.rating,
  images = EXCLUDED.images,
  brand = EXCLUDED.brand,
  sizes = EXCLUDED.sizes,
  description = EXCLUDED.description,
  "isNewArrival" = EXCLUDED."isNewArrival",
  "isTopRated" = EXCLUDED."isTopRated",
  "isBestSeller" = EXCLUDED."isBestSeller",
  "isLimitedEdition" = EXCLUDED."isLimitedEdition";
