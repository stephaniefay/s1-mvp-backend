CREATE TABLE "cards" (
  "id" text NOT NULL,
  "name" text NOT NULL,
  "hp" bigint NOT NULL,
  "number" bigint NOT NULL,
  "rarity" text NOT NULL,
  "image_sm" text,
  "image_lg" text,
  "unlimited" boolean,
  "expanded" boolean,
  "standard" boolean,
  "supertype" bigint NOT NULL,
  PRIMARY KEY ("id")
);

CREATE TABLE "supertype" (
  "id" bigint NOT NULL,
  "type" text NOT NULL,
  PRIMARY KEY ("id")
);

CREATE TABLE "subtype" (
  "id" bigint NOT NULL,
  "type" text NOT NULL,
  PRIMARY KEY ("id")
);

CREATE TABLE "type" (
  "id" bigint NOT NULL,
  "type" text NOT NULL,
  PRIMARY KEY ("id")
);

CREATE TABLE "card_subtype" (
  "id" bigint NOT NULL,
  "card_id" text NOT NULL,
  "subtype_id" bigint NOT NULL,
  PRIMARY KEY ("id")
);

CREATE TABLE "card_type" (
  "id" bigint NOT NULL,
  "card_id" text NOT NULL,
  "type_id" bigint NOT NULL,
  PRIMARY KEY ("id")
);

CREATE TABLE "card_attacks" (
  "id" bigint NOT NULL,
  "card_id" text NOT NULL,
  "attack_id" bigint NOT NULL,
  PRIMARY KEY ("id")
);

CREATE TABLE "card_weaknesses" (
  "id" bigint NOT NULL,
  "card_id" text NOT NULL,
  "weakness_id" bigint NOT NULL,
  PRIMARY KEY ("id")
);

CREATE TABLE "attacks" (
  "id" bigint NOT NULL,
  "name" text NOT NULL,
  "damage" text,
  "text" text,
  PRIMARY KEY ("id")
);

CREATE TABLE "weaknesses" (
  "id" bigint NOT NULL,
  "type" bigint,
  "value" text,
  PRIMARY KEY ("id")
);

CREATE TABLE "cost" (
  "id" bigint NOT NULL,
  "type" bigint,
  "order" bigint,
  "id_ref" text,
  "type_ref" text,
  PRIMARY KEY ("id")
);

CREATE TABLE "set" (
  "id" text NOT NULL,
  "name" text NOT NULL,
  "series" bigint,
  "collection_total" bigint NOT NULL,
  "unlimited" boolean,
  "expanded" boolean,
  "standard" boolean,
  "image_logo" text,
  "image _symbol" text,
  "release_date" date,
  "ptcgo_code" text,
  PRIMARY KEY ("id")
);

CREATE TABLE "series" (
  "id" bigint NOT NULL,
  "name" text NOT NULL,
  "acronym" text NOT NULL,
  PRIMARY KEY ("id")
);

CREATE TABLE "set_card" (
  "id" bigint NOT NULL,
  "set_id" text NOT NULL,
  "card_id" text NOT NULL,
  PRIMARY KEY ("id")
);

CREATE TABLE "wish_card" (
  "id" bigint NOT NULL,
  "wish_id" text NOT NULL,
  "card_id" text NOT NULL,
  PRIMARY KEY ("id")
);

ALTER TABLE "card_subtype" ADD CONSTRAINT "fk_card_subtype_subtype_id_subtype_id" FOREIGN KEY ("subtype_id") REFERENCES "subtype" ("id");

ALTER TABLE "cards" ADD CONSTRAINT "fk_cards_id_card_type_card_id" FOREIGN KEY ("id") REFERENCES "card_type" ("card_id");

ALTER TABLE "cards" ADD CONSTRAINT "fk_cards_id_card_attacks_card_id" FOREIGN KEY ("id") REFERENCES "card_attacks" ("card_id");

ALTER TABLE "cards" ADD CONSTRAINT "fk_cards_id_card_weaknesses_card_id" FOREIGN KEY ("id") REFERENCES "card_weaknesses" ("card_id");

ALTER TABLE "card_attacks" ADD CONSTRAINT "fk_card_attacks_attack_id_attacks_id" FOREIGN KEY ("attack_id") REFERENCES "attacks" ("id");

ALTER TABLE "type" ADD FOREIGN KEY ("id") REFERENCES "card_type" ("type_id");

ALTER TABLE "weaknesses" ADD FOREIGN KEY ("id") REFERENCES "card_weaknesses" ("weakness_id");

ALTER TABLE "cost" ADD FOREIGN KEY ("id_ref") REFERENCES "cards" ("id");

ALTER TABLE "cost" ADD FOREIGN KEY ("id_ref") REFERENCES "weaknesses" ("type");

ALTER TABLE "cost" ADD FOREIGN KEY ("id_ref") REFERENCES "attacks" ("id");

ALTER TABLE "card_subtype" ADD FOREIGN KEY ("card_id") REFERENCES "cards" ("id");

ALTER TABLE "supertype" ADD FOREIGN KEY ("id") REFERENCES "cards" ("supertype");

ALTER TABLE "series" ADD FOREIGN KEY ("id") REFERENCES "set" ("series");

ALTER TABLE "set_card" ADD FOREIGN KEY ("set_id") REFERENCES "set" ("id");

ALTER TABLE "set_card" ADD FOREIGN KEY ("card_id") REFERENCES "cards" ("id");

ALTER TABLE "cards" ADD FOREIGN KEY ("id") REFERENCES "wish_card" ("card_id");
