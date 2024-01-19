PGDMP                          |            report_breach_v1    15.4    15.2 �    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    35192    report_breach_v1    DATABASE     |   CREATE DATABASE report_breach_v1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF-8';
     DROP DATABASE report_breach_v1;
                postgres    false            �           0    0    DATABASE report_breach_v1    COMMENT     k   COMMENT ON DATABASE report_breach_v1 IS 'This database is validating the model designed on the 20231223.';
                   postgres    false    3836            �            1259    35407    company    TABLE     �   CREATE TABLE public.company (
    id integer NOT NULL,
    company_type_id integer DEFAULT 0 NOT NULL,
    name character(50) DEFAULT 'No name yet'::bpchar NOT NULL
);
    DROP TABLE public.company;
       public         heap    postgres    false            �           0    0    TABLE company    COMMENT     ;   COMMENT ON TABLE public.company IS '{semantic:companies}';
          public          postgres    false    226            �            1259    35498    company_non_uk    TABLE     �  CREATE TABLE public.company_non_uk (
    company_id integer NOT NULL,
    website character(100) NOT NULL,
    address_1 character(100) DEFAULT ' '::bpchar NOT NULL,
    address_2 character(100) DEFAULT ' '::bpchar NOT NULL,
    address_3 character(100) DEFAULT ' '::bpchar NOT NULL,
    address_4 character(100) DEFAULT ' '::bpchar,
    city character(50) NOT NULL,
    country character(2) NOT NULL,
    postcode character(20)
);
 "   DROP TABLE public.company_non_uk;
       public         heap    postgres    false            �           0    0    TABLE company_non_uk    COMMENT     �   COMMENT ON TABLE public.company_non_uk IS 'Needs to create an empty  address line with one character. Otherwise contact in sql becomes null
{semantic:companies}';
          public          postgres    false    231            �            1259    35400    company_type    TABLE     �   CREATE TABLE public.company_type (
    id integer NOT NULL,
    short_label character(20) NOT NULL,
    long_label character(100) NOT NULL,
    start_date date DEFAULT CURRENT_DATE NOT NULL,
    end_date date DEFAULT '2999-12-31'::date NOT NULL
);
     DROP TABLE public.company_type;
       public         heap    postgres    false                        0    0    TABLE company_type    COMMENT     �   COMMENT ON TABLE public.company_type IS 'the type indicating whether a company is in company house, uk companies not in company house,  non uk companies.
{semantic:companies}';
          public          postgres    false    225            �            1259    35413    company_uk_ch    TABLE     u   CREATE TABLE public.company_uk_ch (
    company_id integer NOT NULL,
    registered_number character(10) NOT NULL
);
 !   DROP TABLE public.company_uk_ch;
       public         heap    postgres    false                       0    0    TABLE company_uk_ch    COMMENT     R   COMMENT ON TABLE public.company_uk_ch IS 'UK limited company in Companies House';
          public          postgres    false    227                       0    0 &   COLUMN company_uk_ch.registered_number    COMMENT     �   COMMENT ON COLUMN public.company_uk_ch.registered_number IS 'This length may not match CH number. However, it needs to be checked with ICMS and LITE.';
          public          postgres    false    227            �            1259    35467    company_uk_non_ch    TABLE     d  CREATE TABLE public.company_uk_non_ch (
    company_id integer NOT NULL,
    website character(100) NOT NULL,
    address_1 character(100) DEFAULT ' '::bpchar NOT NULL,
    address_2 character(100) DEFAULT ' '::bpchar NOT NULL,
    postcode character(10) NOT NULL,
    city character(50) NOT NULL,
    country character(2) DEFAULT 'GB'::bpchar NOT NULL
);
 %   DROP TABLE public.company_uk_non_ch;
       public         heap    postgres    false            �            1259    35746    companies_list    VIEW     �  CREATE VIEW public.companies_list AS
 SELECT e.short_label AS company_type,
    c.name AS company_name,
    f.registered_number AS company_house_number,
    (('CH address 1'::text || ','::text) || 'CH address 2 '::text) AS address,
    'CH postcode'::bpchar AS postcode,
    'CH city'::bpchar AS city,
    'CH country'::bpchar AS country,
    c.id AS company_id
   FROM ((public.company c
     JOIN public.company_type e ON ((e.id = c.company_type_id)))
     JOIN public.company_uk_ch f ON ((f.company_id = c.id)))
UNION
 SELECT e.short_label AS company_type,
    c.name AS company_name,
    'NO COMPANIES HOUSE NUMBER'::bpchar AS company_house_number,
    (((f.address_1)::text || ','::text) || (f.address_2)::text) AS address,
    f.postcode,
    f.city,
    f.country,
    c.id AS company_id
   FROM ((public.company c
     JOIN public.company_type e ON ((e.id = c.company_type_id)))
     JOIN public.company_uk_non_ch f ON ((f.company_id = c.id)))
UNION
 SELECT e.short_label AS company_type,
    c.name AS company_name,
    'NO COMPANIES HOUSE NUMBER'::bpchar AS company_house_number,
    (((((((f.address_1)::text || ','::text) || (f.address_2)::text) || ','::text) || (f.address_3)::text) || ','::text) || (f.address_4)::text) AS address,
    f.postcode,
    f.city,
    f.country,
    c.id AS company_id
   FROM ((public.company c
     JOIN public.company_type e ON ((e.id = c.company_type_id)))
     JOIN public.company_non_uk f ON ((f.company_id = c.id)));
 !   DROP VIEW public.companies_list;
       public          postgres    false    231    226    225    225    227    230    230    230    230    230    230    231    231    227    226    226    231    231    231    231    231            �            1259    35441    company_role    TABLE     �   CREATE TABLE public.company_role (
    id integer NOT NULL,
    role character(20) NOT NULL,
    start_date date DEFAULT CURRENT_DATE NOT NULL,
    end_date date DEFAULT '2999-12-31'::date NOT NULL
);
     DROP TABLE public.company_role;
       public         heap    postgres    false                       0    0    TABLE company_role    COMMENT     Y   COMMENT ON TABLE public.company_role IS 'the role in the breach. 
{semantic:companies}';
          public          postgres    false    228            �            1259    35264    content    TABLE     �   CREATE TABLE public.content (
    question_id integer NOT NULL,
    report_id integer NOT NULL,
    creation_date date DEFAULT CURRENT_DATE NOT NULL,
    json_answer json NOT NULL,
    schema_id integer DEFAULT 0 NOT NULL
);
    DROP TABLE public.content;
       public         heap    postgres    false                       0    0    TABLE content    COMMENT     I   COMMENT ON TABLE public.content IS 'answers to questions for a report.';
          public          postgres    false    220            �            1259    35590    json_schema    TABLE     p   CREATE TABLE public.json_schema (
    id integer NOT NULL,
    schema text NOT NULL,
    label character(50)
);
    DROP TABLE public.json_schema;
       public         heap    postgres    false            �            1259    35255    question    TABLE     �   CREATE TABLE public.question (
    id integer NOT NULL,
    json_question character(255) NOT NULL,
    start_date date DEFAULT CURRENT_DATE NOT NULL,
    end_date date DEFAULT '2999-12-31'::date NOT NULL,
    schema_id integer DEFAULT 0 NOT NULL
);
    DROP TABLE public.question;
       public         heap    postgres    false                       0    0    TABLE question    COMMENT     �   COMMENT ON TABLE public.question IS 'questions asked to the reporters.  We use JSON to model the answers. It is simplifies the answers and model. ';
          public          postgres    false    219            �            1259    35235    report    TABLE       CREATE TABLE public.report (
    id integer NOT NULL,
    creation_date date DEFAULT CURRENT_DATE NOT NULL,
    regime_id integer DEFAULT 0 NOT NULL,
    type_id integer DEFAULT 1 NOT NULL,
    unique_ref character(6) NOT NULL,
    start_breach_date date,
    end_breach_date date
);
    DROP TABLE public.report;
       public         heap    postgres    false            �            1259    35783    content_list    VIEW     �  CREATE VIEW public.content_list AS
 SELECT e.unique_ref,
    b.json_question AS question,
    c.json_answer AS answer,
    e.id AS report_id
   FROM ((((public.json_schema a
     JOIN public.question b ON ((a.id = b.schema_id)))
     JOIN public.content c ON ((c.question_id = b.id)))
     JOIN public.json_schema d ON ((d.id = c.schema_id)))
     JOIN public.report e ON ((e.id = c.report_id)));
    DROP VIEW public.content_list;
       public          postgres    false    219    217    217    219    232    220    220    220    220    219            �            1259    35243    document    TABLE     �   CREATE TABLE public.document (
    report_id integer NOT NULL,
    ref integer NOT NULL,
    creation_date date DEFAULT CURRENT_TIMESTAMP NOT NULL,
    path character(255) NOT NULL
);
    DROP TABLE public.document;
       public         heap    postgres    false                       0    0    TABLE document    COMMENT     U   COMMENT ON TABLE public.document IS 'Stores the path to documents stored securely.';
          public          postgres    false    218            �            1259    35779    documents_list    VIEW     �   CREATE VIEW public.documents_list AS
 SELECT b.unique_ref,
    a.ref AS document_ref,
    a.creation_date AS document_creation_date,
    a.path,
    b.id AS report_id
   FROM (public.document a
     JOIN public.report b ON ((a.report_id = b.id)));
 !   DROP VIEW public.documents_list;
       public          postgres    false    218    218    218    218    217    217            �            1259    35212    other_regime    TABLE     �   CREATE TABLE public.other_regime (
    regime_id integer DEFAULT 1 NOT NULL,
    description character(100) NOT NULL,
    report_id integer NOT NULL
);
     DROP TABLE public.other_regime;
       public         heap    postgres    false                       0    0    TABLE other_regime    COMMENT     R   COMMENT ON TABLE public.other_regime IS 'stores other regime typed by the users';
          public          postgres    false    215            �            1259    35193    regime    TABLE       CREATE TABLE public.regime (
    id integer NOT NULL,
    short_name character(20) NOT NULL,
    full_name character(100) NOT NULL,
    start_date date NOT NULL,
    end_date date DEFAULT '2999-12-31'::date NOT NULL,
    shown_gui_flag boolean DEFAULT true NOT NULL
);
    DROP TABLE public.regime;
       public         heap    postgres    false                       0    0    TABLE regime    COMMENT     �   COMMENT ON TABLE public.regime IS 'List of regime and countries under trading sanctions.  This table refers to legislation with a start and end date. ';
          public          postgres    false    214            	           0    0    COLUMN regime.short_name    COMMENT     m   COMMENT ON COLUMN public.regime.short_name IS 'Legal short name used for analytical purposes for grouping.';
          public          postgres    false    214            
           0    0    COLUMN regime.full_name    COMMENT     r   COMMENT ON COLUMN public.regime.full_name IS 'Regime label shown on the front end to support user interaction. ';
          public          postgres    false    214                       0    0    COLUMN regime.start_date    COMMENT     W   COMMENT ON COLUMN public.regime.start_date IS 'start of the legislation application.';
          public          postgres    false    214                       0    0    COLUMN regime.end_date    COMMENT     Y   COMMENT ON COLUMN public.regime.end_date IS 'date the legislation stop its application';
          public          postgres    false    214                       0    0    COLUMN regime.shown_gui_flag    COMMENT     u   COMMENT ON COLUMN public.regime.shown_gui_flag IS 'boolean flag indicating whether the regime shown to the users. ';
          public          postgres    false    214            �            1259    35732    regimes_list    VIEW       CREATE VIEW public.regimes_list AS
 SELECT regime.id,
    regime.short_name,
    regime.full_name,
    regime.start_date,
    regime.end_date,
    regime.shown_gui_flag,
    'No other description'::bpchar AS other_description
   FROM public.regime
  WHERE (NOT (regime.id = 1))
UNION
 SELECT a.id,
    a.short_name,
    a.full_name,
    a.start_date,
    a.end_date,
    a.shown_gui_flag,
    b.description AS other_description
   FROM (public.regime a
     JOIN public.other_regime b ON ((a.id = b.regime_id)))
  WHERE (a.id = 1);
    DROP VIEW public.regimes_list;
       public          postgres    false    215    214    214    214    214    214    214    215            �            1259    35302    relationship    TABLE     (  CREATE TABLE public.relationship (
    id integer NOT NULL,
    short_name character(20) NOT NULL,
    full_name character(150) NOT NULL,
    start_date date DEFAULT CURRENT_DATE NOT NULL,
    end_date date DEFAULT '2999-12-31'::date NOT NULL,
    shown_gui_flag boolean DEFAULT true NOT NULL
);
     DROP TABLE public.relationship;
       public         heap    postgres    false                       0    0    TABLE relationship    COMMENT     T   COMMENT ON TABLE public.relationship IS 'the reporter relationship to the company';
          public          postgres    false    221            �            1259    35448    report_company    TABLE     �   CREATE TABLE public.report_company (
    report_id integer NOT NULL,
    company_id integer NOT NULL,
    company_role_id integer NOT NULL
);
 "   DROP TABLE public.report_company;
       public         heap    postgres    false            �            1259    35794    report_companies_list    VIEW     �  CREATE VIEW public.report_companies_list AS
 SELECT a.unique_ref,
    c.name AS company_name,
    e.short_label AS company_type,
    d.role
   FROM ((((public.report a
     JOIN public.report_company b ON ((a.id = b.report_id)))
     JOIN public.company c ON ((c.id = b.company_id)))
     JOIN public.company_role d ON ((d.id = b.company_role_id)))
     JOIN public.company_type e ON ((e.id = c.company_type_id)));
 (   DROP VIEW public.report_companies_list;
       public          postgres    false    229    217    217    225    225    226    226    226    228    228    229    229                       0    0    VIEW report_companies_list    COMMENT     r   COMMENT ON VIEW public.report_companies_list IS 'It should be refined once we understand better the user needs.';
          public          postgres    false    240            �            1259    35799    report_questions_list    VIEW     �  CREATE VIEW public.report_questions_list AS
 SELECT e.unique_ref,
    b.json_question AS question,
    a.schema AS question_schema,
    c.json_answer AS answer,
    d.schema AS answer_schema
   FROM ((((public.json_schema a
     JOIN public.question b ON ((a.id = b.schema_id)))
     JOIN public.content c ON ((c.question_id = b.id)))
     JOIN public.json_schema d ON ((d.id = c.schema_id)))
     JOIN public.report e ON ((e.id = c.report_id)));
 (   DROP VIEW public.report_questions_list;
       public          postgres    false    220    232    232    220    220    220    217    217    219    219    219            �            1259    35326    report_reporter    TABLE     �   CREATE TABLE public.report_reporter (
    report_id integer NOT NULL,
    reporter_id integer NOT NULL,
    relationship_id integer NOT NULL
);
 #   DROP TABLE public.report_reporter;
       public         heap    postgres    false                       0    0    TABLE report_reporter    COMMENT     �   COMMENT ON TABLE public.report_reporter IS 'created a many to many relationship for future proofing and avoid duplication of data.';
          public          postgres    false    223            �            1259    35229    report_type    TABLE     �   CREATE TABLE public.report_type (
    id integer NOT NULL,
    short_label character(20) NOT NULL,
    start_date date NOT NULL,
    end_date date DEFAULT '2999-12-31'::date NOT NULL
);
    DROP TABLE public.report_type;
       public         heap    postgres    false            �            1259    35314    reporter    TABLE     �   CREATE TABLE public.reporter (
    id integer NOT NULL,
    full_name character(50) NOT NULL,
    email character(50) DEFAULT 'no email yet'::bpchar NOT NULL,
    email_verified boolean DEFAULT false NOT NULL
);
    DROP TABLE public.reporter;
       public         heap    postgres    false                       0    0    TABLE reporter    COMMENT     H   COMMENT ON TABLE public.reporter IS 'the person who report the breach';
          public          postgres    false    222                       0    0    COLUMN reporter.full_name    COMMENT     n   COMMENT ON COLUMN public.reporter.full_name IS 'The length is not relevant.  it is fine to make it longer. ';
          public          postgres    false    222                       0    0    COLUMN reporter.email    COMMENT     O   COMMENT ON COLUMN public.reporter.email IS 'increase the length as you wish.';
          public          postgres    false    222            �            1259    35336    verification_code    TABLE     J  CREATE TABLE public.verification_code (
    reporter_id integer NOT NULL,
    creation_date_time date DEFAULT CURRENT_TIMESTAMP NOT NULL,
    expiry_date_time date DEFAULT (CURRENT_TIMESTAMP + '1 day'::interval) NOT NULL,
    succesful_verification_date date DEFAULT '2999-12-31'::date NOT NULL,
    code character(6) NOT NULL
);
 %   DROP TABLE public.verification_code;
       public         heap    postgres    false                       0    0    TABLE verification_code    COMMENT     g   COMMENT ON TABLE public.verification_code IS 'contains generated code with successful verification. ';
          public          postgres    false    224                       0    0    COLUMN verification_code.code    COMMENT     �   COMMENT ON COLUMN public.verification_code.code IS 'This code is generated randomly. The length can vary from the one used here for testing.';
          public          postgres    false    224            �            1259    35741    reporters_list    VIEW     �  CREATE VIEW public.reporters_list AS
 SELECT a.id AS reporter_id,
    a.full_name AS reporter,
    a.email AS emailed,
    a.email_verified AS successfully_verified,
    b.creation_date_time AS code_sent,
    b.expiry_date_time AS expiry_code_date,
    b.succesful_verification_date AS verification_date,
    'VERIFIED'::text AS status
   FROM (public.reporter a
     JOIN public.verification_code b ON ((a.id = b.reporter_id)))
  WHERE (a.email_verified = true)
UNION
 SELECT a.id AS reporter_id,
    a.full_name AS reporter,
    a.email AS emailed,
    a.email_verified AS successfully_verified,
    b.creation_date_time AS code_sent,
    b.expiry_date_time AS expiry_code_date,
    b.succesful_verification_date AS verification_date,
    'NOT VERIFIED'::text AS status
   FROM (public.reporter a
     JOIN public.verification_code b ON ((a.id = b.reporter_id)))
  WHERE (a.email_verified = false);
 !   DROP VIEW public.reporters_list;
       public          postgres    false    222    224    222    222    224    224    224    222            �            1259    35789    reports_and_reporters_list    VIEW     �  CREATE VIEW public.reports_and_reporters_list AS
 SELECT b.unique_ref,
    c.full_name AS reporter,
    c.email AS emailed,
    c.email_verified AS successfully_verified,
    e.creation_date_time AS code_sent,
    e.expiry_date_time AS expiry_code_date,
    e.succesful_verification_date AS verification_date,
    d.short_name AS relationship
   FROM ((((public.report_reporter a
     JOIN public.report b ON ((b.id = a.report_id)))
     JOIN public.reporter c ON ((c.id = a.reporter_id)))
     JOIN public.relationship d ON ((d.id = a.relationship_id)))
     JOIN public.verification_code e ON ((c.id = e.reporter_id)))
  WHERE (c.email_verified = true)
UNION
 SELECT b.unique_ref,
    c.full_name AS reporter,
    c.email AS emailed,
    c.email_verified AS successfully_verified,
    e.creation_date_time AS code_sent,
    e.expiry_date_time AS expiry_code_date,
    e.succesful_verification_date AS verification_date,
    d.short_name AS relationship
   FROM ((((public.report_reporter a
     JOIN public.report b ON ((b.id = a.report_id)))
     JOIN public.reporter c ON ((c.id = a.reporter_id)))
     JOIN public.relationship d ON ((d.id = a.relationship_id)))
     JOIN public.verification_code e ON ((c.id = e.reporter_id)))
  WHERE (c.email_verified = false);
 -   DROP VIEW public.reports_and_reporters_list;
       public          postgres    false    217    224    224    224    224    223    223    223    222    222    222    222    221    221    217            �            1259    35762    reports_list    VIEW     �  CREATE VIEW public.reports_list AS
 SELECT a.unique_ref,
    a.id AS report_id,
    a.creation_date AS breach_reported_date,
    b.short_label AS report_type,
    c.full_name AS regime
   FROM ((public.report a
     JOIN public.report_type b ON ((a.type_id = b.id)))
     JOIN public.regime c ON ((c.id = a.regime_id)))
  WHERE (NOT (c.id = 1))
UNION
 SELECT a.unique_ref,
    a.id AS report_id,
    a.creation_date AS breach_reported_date,
    b.short_label AS report_type,
    (((c.full_name)::text || ' - '::text) || (d.description)::text) AS regime
   FROM (((public.report a
     JOIN public.report_type b ON ((a.type_id = b.id)))
     JOIN public.regime c ON ((c.id = a.regime_id)))
     JOIN public.other_regime d ON ((d.report_id = a.id)));
    DROP VIEW public.reports_list;
       public          postgres    false    216    214    214    215    215    216    217    217    217    217    217            �          0    35407    company 
   TABLE DATA           <   COPY public.company (id, company_type_id, name) FROM stdin;
    public          postgres    false    226   D�       �          0    35498    company_non_uk 
   TABLE DATA           �   COPY public.company_non_uk (company_id, website, address_1, address_2, address_3, address_4, city, country, postcode) FROM stdin;
    public          postgres    false    231   ��       �          0    35441    company_role 
   TABLE DATA           F   COPY public.company_role (id, role, start_date, end_date) FROM stdin;
    public          postgres    false    228   r�       �          0    35400    company_type 
   TABLE DATA           Y   COPY public.company_type (id, short_label, long_label, start_date, end_date) FROM stdin;
    public          postgres    false    225   ʾ       �          0    35413    company_uk_ch 
   TABLE DATA           F   COPY public.company_uk_ch (company_id, registered_number) FROM stdin;
    public          postgres    false    227   ��       �          0    35467    company_uk_non_ch 
   TABLE DATA           o   COPY public.company_uk_non_ch (company_id, website, address_1, address_2, postcode, city, country) FROM stdin;
    public          postgres    false    230   ��       �          0    35264    content 
   TABLE DATA           `   COPY public.content (question_id, report_id, creation_date, json_answer, schema_id) FROM stdin;
    public          postgres    false    220   �       �          0    35243    document 
   TABLE DATA           G   COPY public.document (report_id, ref, creation_date, path) FROM stdin;
    public          postgres    false    218   ��       �          0    35590    json_schema 
   TABLE DATA           8   COPY public.json_schema (id, schema, label) FROM stdin;
    public          postgres    false    232   b�       �          0    35212    other_regime 
   TABLE DATA           I   COPY public.other_regime (regime_id, description, report_id) FROM stdin;
    public          postgres    false    215   
�       �          0    35255    question 
   TABLE DATA           V   COPY public.question (id, json_question, start_date, end_date, schema_id) FROM stdin;
    public          postgres    false    219   j�       �          0    35193    regime 
   TABLE DATA           a   COPY public.regime (id, short_name, full_name, start_date, end_date, shown_gui_flag) FROM stdin;
    public          postgres    false    214   ��       �          0    35302    relationship 
   TABLE DATA           g   COPY public.relationship (id, short_name, full_name, start_date, end_date, shown_gui_flag) FROM stdin;
    public          postgres    false    221   ��       �          0    35235    report 
   TABLE DATA           w   COPY public.report (id, creation_date, regime_id, type_id, unique_ref, start_breach_date, end_breach_date) FROM stdin;
    public          postgres    false    217   �       �          0    35448    report_company 
   TABLE DATA           P   COPY public.report_company (report_id, company_id, company_role_id) FROM stdin;
    public          postgres    false    229   r�       �          0    35326    report_reporter 
   TABLE DATA           R   COPY public.report_reporter (report_id, reporter_id, relationship_id) FROM stdin;
    public          postgres    false    223   ��       �          0    35229    report_type 
   TABLE DATA           L   COPY public.report_type (id, short_label, start_date, end_date) FROM stdin;
    public          postgres    false    216   ��       �          0    35314    reporter 
   TABLE DATA           H   COPY public.reporter (id, full_name, email, email_verified) FROM stdin;
    public          postgres    false    222   =�       �          0    35336    verification_code 
   TABLE DATA           �   COPY public.verification_code (reporter_id, creation_date_time, expiry_date_time, succesful_verification_date, code) FROM stdin;
    public          postgres    false    224   ��       7           2606    35504 "   company_non_uk company_non_uk_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.company_non_uk
    ADD CONSTRAINT company_non_uk_pkey PRIMARY KEY (company_id);
 L   ALTER TABLE ONLY public.company_non_uk DROP CONSTRAINT company_non_uk_pkey;
       public            postgres    false    231            '           2606    35412    company company_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.company DROP CONSTRAINT company_pkey;
       public            postgres    false    226            -           2606    35447    company_role company_role_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.company_role
    ADD CONSTRAINT company_role_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.company_role DROP CONSTRAINT company_role_pkey;
       public            postgres    false    228            %           2606    35406    company_type company_type_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.company_type
    ADD CONSTRAINT company_type_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.company_type DROP CONSTRAINT company_type_pkey;
       public            postgres    false    225            *           2606    35417     company_uk_ch company_uk_ch_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.company_uk_ch
    ADD CONSTRAINT company_uk_ch_pkey PRIMARY KEY (company_id);
 J   ALTER TABLE ONLY public.company_uk_ch DROP CONSTRAINT company_uk_ch_pkey;
       public            postgres    false    227            4           2606    35471 (   company_uk_non_ch company_uk_non_ch_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.company_uk_non_ch
    ADD CONSTRAINT company_uk_non_ch_pkey PRIMARY KEY (company_id);
 R   ALTER TABLE ONLY public.company_uk_non_ch DROP CONSTRAINT company_uk_non_ch_pkey;
       public            postgres    false    230                       2606    35271    content content_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.content
    ADD CONSTRAINT content_pkey PRIMARY KEY (question_id, report_id);
 >   ALTER TABLE ONLY public.content DROP CONSTRAINT content_pkey;
       public            postgres    false    220    220                       2606    35772    document document_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.document
    ADD CONSTRAINT document_pkey PRIMARY KEY (report_id, ref, creation_date);
 @   ALTER TABLE ONLY public.document DROP CONSTRAINT document_pkey;
       public            postgres    false    218    218    218            :           2606    35596    json_schema json_schema_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.json_schema
    ADD CONSTRAINT json_schema_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.json_schema DROP CONSTRAINT json_schema_pkey;
       public            postgres    false    232                       2606    35761    other_regime other_regime_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.other_regime
    ADD CONSTRAINT other_regime_pkey PRIMARY KEY (regime_id, report_id);
 H   ALTER TABLE ONLY public.other_regime DROP CONSTRAINT other_regime_pkey;
       public            postgres    false    215    215                       2606    35263    question question_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.question DROP CONSTRAINT question_pkey;
       public            postgres    false    219            �           2606    35197    regime regime_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.regime
    ADD CONSTRAINT regime_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.regime DROP CONSTRAINT regime_pkey;
       public            postgres    false    214            �           2606    35206    regime regime_short_name 
   CONSTRAINT     n   ALTER TABLE ONLY public.regime
    ADD CONSTRAINT regime_short_name UNIQUE (short_name) INCLUDE (short_name);
 B   ALTER TABLE ONLY public.regime DROP CONSTRAINT regime_short_name;
       public            postgres    false    214                       0    0 &   CONSTRAINT regime_short_name ON regime    COMMENT     X   COMMENT ON CONSTRAINT regime_short_name ON public.regime IS 'The short name is unique';
          public          postgres    false    3583                       2606    35308    relationship relationship_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.relationship
    ADD CONSTRAINT relationship_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.relationship DROP CONSTRAINT relationship_pkey;
       public            postgres    false    221            2           2606    35452 "   report_company report_company_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.report_company
    ADD CONSTRAINT report_company_pkey PRIMARY KEY (report_id, company_id, company_role_id);
 L   ALTER TABLE ONLY public.report_company DROP CONSTRAINT report_company_pkey;
       public            postgres    false    229    229    229                       2606    35242    report report_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.report
    ADD CONSTRAINT report_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.report DROP CONSTRAINT report_pkey;
       public            postgres    false    217                        2606    35330 $   report_reporter report_reporter_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.report_reporter
    ADD CONSTRAINT report_reporter_pkey PRIMARY KEY (report_id, reporter_id, relationship_id);
 N   ALTER TABLE ONLY public.report_reporter DROP CONSTRAINT report_reporter_pkey;
       public            postgres    false    223    223    223            
           2606    35234    report_type report_type_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.report_type
    ADD CONSTRAINT report_type_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.report_type DROP CONSTRAINT report_type_pkey;
       public            postgres    false    216                       2606    35318    reporter reporter_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.reporter
    ADD CONSTRAINT reporter_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.reporter DROP CONSTRAINT reporter_pkey;
       public            postgres    false    222                       2606    35740    regime unique_fullname 
   CONSTRAINT     j   ALTER TABLE ONLY public.regime
    ADD CONSTRAINT unique_fullname UNIQUE (full_name) INCLUDE (full_name);
 @   ALTER TABLE ONLY public.regime DROP CONSTRAINT unique_fullname;
       public            postgres    false    214                       2606    35738    regime unique_short_name 
   CONSTRAINT     n   ALTER TABLE ONLY public.regime
    ADD CONSTRAINT unique_short_name UNIQUE (short_name) INCLUDE (short_name);
 B   ALTER TABLE ONLY public.regime DROP CONSTRAINT unique_short_name;
       public            postgres    false    214            #           2606    35341 (   verification_code verification_code_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.verification_code
    ADD CONSTRAINT verification_code_pkey PRIMARY KEY (reporter_id, creation_date_time);
 R   ALTER TABLE ONLY public.verification_code DROP CONSTRAINT verification_code_pkey;
       public            postgres    false    224    224            (           1259    35630    fki_companies_companies_type_fk    INDEX     ^   CREATE INDEX fki_companies_companies_type_fk ON public.company USING btree (company_type_id);
 3   DROP INDEX public.fki_companies_companies_type_fk;
       public            postgres    false    226            8           1259    35636    fki_company_company_non_uk    INDEX     [   CREATE INDEX fki_company_company_non_uk ON public.company_non_uk USING btree (company_id);
 .   DROP INDEX public.fki_company_company_non_uk;
       public            postgres    false    231            .           1259    35701    fki_company_company_role    INDEX     ^   CREATE INDEX fki_company_company_role ON public.report_company USING btree (company_role_id);
 ,   DROP INDEX public.fki_company_company_role;
       public            postgres    false    229            +           1259    35642    fki_company_company_uk_ch    INDEX     Y   CREATE INDEX fki_company_company_uk_ch ON public.company_uk_ch USING btree (company_id);
 -   DROP INDEX public.fki_company_company_uk_ch;
       public            postgres    false    227            5           1259    35648    fki_company_company_uk_non_ch    INDEX     a   CREATE INDEX fki_company_company_uk_non_ch ON public.company_uk_non_ch USING btree (company_id);
 1   DROP INDEX public.fki_company_company_uk_non_ch;
       public            postgres    false    230                       1259    35660    fki_content_question_fk    INDEX     R   CREATE INDEX fki_content_question_fk ON public.content USING btree (question_id);
 +   DROP INDEX public.fki_content_question_fk;
       public            postgres    false    220                       1259    35654    fki_content_report    INDEX     K   CREATE INDEX fki_content_report ON public.content USING btree (report_id);
 &   DROP INDEX public.fki_content_report;
       public            postgres    false    220                       1259    35222    fki_regime_other_regime    INDEX     U   CREATE INDEX fki_regime_other_regime ON public.other_regime USING btree (regime_id);
 +   DROP INDEX public.fki_regime_other_regime;
       public            postgres    false    215                       1259    35672    fki_regime_regime_other    INDEX     U   CREATE INDEX fki_regime_regime_other ON public.other_regime USING btree (regime_id);
 +   DROP INDEX public.fki_regime_regime_other;
       public            postgres    false    215            /           1259    35684    fki_report_company    INDEX     S   CREATE INDEX fki_report_company ON public.report_company USING btree (company_id);
 &   DROP INDEX public.fki_report_company;
       public            postgres    false    229                       1259    35778    fki_report_document    INDEX     M   CREATE INDEX fki_report_document ON public.document USING btree (report_id);
 '   DROP INDEX public.fki_report_document;
       public            postgres    false    218                       1259    35757    fki_report_other_regime    INDEX     U   CREATE INDEX fki_report_other_regime ON public.other_regime USING btree (report_id);
 +   DROP INDEX public.fki_report_other_regime;
       public            postgres    false    215                       1259    35624    fki_report_regime_fk    INDEX     L   CREATE INDEX fki_report_regime_fk ON public.report USING btree (regime_id);
 (   DROP INDEX public.fki_report_regime_fk;
       public            postgres    false    217            0           1259    35678    fki_report_report_company    INDEX     Y   CREATE INDEX fki_report_report_company ON public.report_company USING btree (report_id);
 -   DROP INDEX public.fki_report_report_company;
       public            postgres    false    229                       1259    35618    fki_report_report_id_fk    INDEX     M   CREATE INDEX fki_report_report_id_fk ON public.report USING btree (type_id);
 +   DROP INDEX public.fki_report_report_id_fk;
       public            postgres    false    217                       1259    35690    fki_report_reporter    INDEX     T   CREATE INDEX fki_report_reporter ON public.report_reporter USING btree (report_id);
 '   DROP INDEX public.fki_report_reporter;
       public            postgres    false    223                       1259    35713     fki_report_reporter_relationship    INDEX     g   CREATE INDEX fki_report_reporter_relationship ON public.report_reporter USING btree (relationship_id);
 4   DROP INDEX public.fki_report_reporter_relationship;
       public            postgres    false    223                       1259    35707    fki_report_reporter_reporter    INDEX     _   CREATE INDEX fki_report_reporter_reporter ON public.report_reporter USING btree (reporter_id);
 0   DROP INDEX public.fki_report_reporter_reporter;
       public            postgres    false    223            !           1259    35719    fki_verification_code_reporter    INDEX     c   CREATE INDEX fki_verification_code_reporter ON public.verification_code USING btree (reporter_id);
 2   DROP INDEX public.fki_verification_code_reporter;
       public            postgres    false    224            F           2606    35625 #   company companies_companies_type_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.company
    ADD CONSTRAINT companies_companies_type_fk FOREIGN KEY (company_type_id) REFERENCES public.company_type(id) NOT VALID;
 M   ALTER TABLE ONLY public.company DROP CONSTRAINT companies_companies_type_fk;
       public          postgres    false    226    3621    225            L           2606    35631 %   company_non_uk company_company_non_uk    FK CONSTRAINT     �   ALTER TABLE ONLY public.company_non_uk
    ADD CONSTRAINT company_company_non_uk FOREIGN KEY (company_id) REFERENCES public.company(id) NOT VALID;
 O   ALTER TABLE ONLY public.company_non_uk DROP CONSTRAINT company_company_non_uk;
       public          postgres    false    226    3623    231            H           2606    35696 #   report_company company_company_role    FK CONSTRAINT     �   ALTER TABLE ONLY public.report_company
    ADD CONSTRAINT company_company_role FOREIGN KEY (company_role_id) REFERENCES public.company_role(id) MATCH FULL NOT VALID;
 M   ALTER TABLE ONLY public.report_company DROP CONSTRAINT company_company_role;
       public          postgres    false    229    228    3629            G           2606    35637 #   company_uk_ch company_company_uk_ch    FK CONSTRAINT     �   ALTER TABLE ONLY public.company_uk_ch
    ADD CONSTRAINT company_company_uk_ch FOREIGN KEY (company_id) REFERENCES public.company(id) NOT VALID;
 M   ALTER TABLE ONLY public.company_uk_ch DROP CONSTRAINT company_company_uk_ch;
       public          postgres    false    3623    227    226            K           2606    35643 +   company_uk_non_ch company_company_uk_non_ch    FK CONSTRAINT     �   ALTER TABLE ONLY public.company_uk_non_ch
    ADD CONSTRAINT company_company_uk_non_ch FOREIGN KEY (company_id) REFERENCES public.company(id) MATCH FULL NOT VALID;
 U   ALTER TABLE ONLY public.company_uk_non_ch DROP CONSTRAINT company_company_uk_non_ch;
       public          postgres    false    230    226    3623            @           2606    35655    content content_question_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.content
    ADD CONSTRAINT content_question_fk FOREIGN KEY (question_id) REFERENCES public.question(id) MATCH FULL NOT VALID;
 E   ALTER TABLE ONLY public.content DROP CONSTRAINT content_question_fk;
       public          postgres    false    219    220    3603            A           2606    35649    content content_report    FK CONSTRAINT     �   ALTER TABLE ONLY public.content
    ADD CONSTRAINT content_report FOREIGN KEY (report_id) REFERENCES public.report(id) NOT VALID;
 @   ALTER TABLE ONLY public.content DROP CONSTRAINT content_report;
       public          postgres    false    220    3598    217            ;           2606    35667     other_regime regime_regime_other    FK CONSTRAINT     �   ALTER TABLE ONLY public.other_regime
    ADD CONSTRAINT regime_regime_other FOREIGN KEY (regime_id) REFERENCES public.regime(id) MATCH FULL NOT VALID;
 J   ALTER TABLE ONLY public.other_regime DROP CONSTRAINT regime_regime_other;
       public          postgres    false    214    215    3581            I           2606    35679    report_company report_company    FK CONSTRAINT     �   ALTER TABLE ONLY public.report_company
    ADD CONSTRAINT report_company FOREIGN KEY (company_id) REFERENCES public.company(id) MATCH FULL NOT VALID;
 G   ALTER TABLE ONLY public.report_company DROP CONSTRAINT report_company;
       public          postgres    false    229    3623    226            ?           2606    35773    document report_document    FK CONSTRAINT     �   ALTER TABLE ONLY public.document
    ADD CONSTRAINT report_document FOREIGN KEY (report_id) REFERENCES public.report(id) MATCH FULL NOT VALID;
 B   ALTER TABLE ONLY public.document DROP CONSTRAINT report_document;
       public          postgres    false    3598    217    218            <           2606    35752     other_regime report_other_regime    FK CONSTRAINT     �   ALTER TABLE ONLY public.other_regime
    ADD CONSTRAINT report_other_regime FOREIGN KEY (report_id) REFERENCES public.report(id) NOT VALID;
 J   ALTER TABLE ONLY public.other_regime DROP CONSTRAINT report_other_regime;
       public          postgres    false    215    3598    217            =           2606    35619    report report_regime_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.report
    ADD CONSTRAINT report_regime_fk FOREIGN KEY (regime_id) REFERENCES public.regime(id) MATCH FULL NOT VALID;
 A   ALTER TABLE ONLY public.report DROP CONSTRAINT report_regime_fk;
       public          postgres    false    217    214    3581            J           2606    35673 $   report_company report_report_company    FK CONSTRAINT     �   ALTER TABLE ONLY public.report_company
    ADD CONSTRAINT report_report_company FOREIGN KEY (report_id) REFERENCES public.report(id) MATCH FULL NOT VALID;
 N   ALTER TABLE ONLY public.report_company DROP CONSTRAINT report_report_company;
       public          postgres    false    217    3598    229            >           2606    35613    report report_report_id_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.report
    ADD CONSTRAINT report_report_id_fk FOREIGN KEY (type_id) REFERENCES public.report_type(id) MATCH FULL NOT VALID;
 D   ALTER TABLE ONLY public.report DROP CONSTRAINT report_report_id_fk;
       public          postgres    false    217    3594    216            B           2606    35691    report_reporter report_reporter    FK CONSTRAINT     �   ALTER TABLE ONLY public.report_reporter
    ADD CONSTRAINT report_reporter FOREIGN KEY (report_id) REFERENCES public.report(id) NOT VALID;
 I   ALTER TABLE ONLY public.report_reporter DROP CONSTRAINT report_reporter;
       public          postgres    false    217    223    3598            C           2606    35708 ,   report_reporter report_reporter_relationship    FK CONSTRAINT     �   ALTER TABLE ONLY public.report_reporter
    ADD CONSTRAINT report_reporter_relationship FOREIGN KEY (relationship_id) REFERENCES public.relationship(id) MATCH FULL NOT VALID;
 V   ALTER TABLE ONLY public.report_reporter DROP CONSTRAINT report_reporter_relationship;
       public          postgres    false    3609    223    221            D           2606    35702 (   report_reporter report_reporter_reporter    FK CONSTRAINT     �   ALTER TABLE ONLY public.report_reporter
    ADD CONSTRAINT report_reporter_reporter FOREIGN KEY (reporter_id) REFERENCES public.reporter(id) MATCH FULL NOT VALID;
 R   ALTER TABLE ONLY public.report_reporter DROP CONSTRAINT report_reporter_reporter;
       public          postgres    false    3611    222    223            E           2606    35714 ,   verification_code verification_code_reporter    FK CONSTRAINT     �   ALTER TABLE ONLY public.verification_code
    ADD CONSTRAINT verification_code_reporter FOREIGN KEY (reporter_id) REFERENCES public.reporter(id) MATCH FULL NOT VALID;
 V   ALTER TABLE ONLY public.verification_code DROP CONSTRAINT verification_code_reporter;
       public          postgres    false    222    3611    224            �   V   x�3�4�t��-H̫T���R pq��9:9�͘����чXm&@m�
E��ř�y
�Pj3i��/�H-"A3�y�b���� !0AW      �   �   x�3��())(���///��H�)OM*�,I�K��U���I�/��IQ�OJ-*�Q020���0K�n��$1>/?/�4;>9���8-��FƘQ�e����I����ʩ(Q���(5��zFb����CK|���I��ih`�!�e�-UVV���ao	���C��[*���ME��rS�1�8W� }�Q�      �   H   x�3�,.-.HM.IMQ(.-(��L-RP�4202�50�54�4����54�56�2BR\���Y���W�Kq� ��      �   �   x����� �gx�{�`�Ν�5!T/�X����=�ژM����_�����ԡ�0�2��5��"�Dd��0���ȥ����,�T��\���Uh;�Fm����	�u	k�����ń=��Kvռ��b�f#���>9�^��jp~>�-�A^���<wa��bL]��V��F��s� l�}r      �      x�3�4��=... ��      �   E   x�3��())(���///�K,OM*�,I�K��U�"दak������E�����YRI�nw'�=... u�7Y      �   �   x�u�1!��Y���ܧ^\Mm]����H}�\*x
E���&ݟ^ @d/u�Cy���7��[t�>�%8�!@e��TzX�d21��1���@݀{����P՜K���z��z��o�N&���l���G�8��+��<z��/-GUH      �   �   x��1!D��^ X��o��A�qI����_�l4�q_7��ˈNt��#��S���(�q���B4�,�e�����O%�U�Tk*�[k�`:ڔ1��L����0�	�H-�3PMg��>{�.҄�^2���k����gt
[|Y��/!�B�/���      �   �   x����
�0���S�����|�05h@ۚF�}w��Q��CHH���V=��I�)�R��j�:O�ZbPa��u����7������m�|����7�w��>/�e�e�+��%8rJc,�X�#<9 �����NYg���1댿k51�� nEu�      �   P   x�3�t��/�H-R(JM��MU(�,HMQH�T 
�
�J��NC.C�����r�M�
�y
A��ř����i�9W� �(�      �     x�Փ�N�@�k�S������L��gH�o�O����$X�w�v\ ��t��-��L����H>hk����ڣ�сZ�H�y��+pE�t�;_�=ᤛ�HA�#9]�_���׬Dl�6�div���(�L�y�&~�!��H�d��Ҝ^r�7�BM���/Oet:�(��kG2k�L>�	�.�RŦ1����0�k-����r4�s0w���Ҷ�4=�CG�[�Sm�JE��G�Q�R=;�e=T��)\~H׃6�U<�`c�z����?Ǿ@&g�k��'/��      �   �   x����k� ����2Ԏ@�)�&l3SvיD�i����_	�#+���w���~	E��x�S(�W�x�� �)�!��F,I���hEQ�U�K(�&���Eh� �n̻���
�w�,��R�c��i�j5�u�*k|PR�}0��%,���	K(u3vj:��ՋLl�t���!-�r����T�~|��\kݩa�g�hr��&s�8��D��O��1L�u� h�m���y�/{���߫�������      �   Y  x�͓Qn�0���)| �v=B�0	�` j�QH[q���4�Ӥv���~���M��t"��Ka��bt�6X�?(���.I�$�T���,O����L�{�#�DAw��t� �1p]�R����|�Pr�k�ޚ����3��R�(W�g�ڍE���~���(��NP�
x�1c8��-q�5 ��4��j+9:}B��u�9V{ôyU���qU�k���~X�5̎��Hm���3�h���B�i���;��8��".�w3���6�V_&��q�� � ���Xv�,S#���ou��0Ż�8��Ɏk�$�"�i�B����s%)�tJ�f�c.��&��O"du      �   ^   x�m�=
�0๹K%�:���J�[I!�l/<
��)���͢)���W�Mū�rW��M/�M�n�Z�4��t�����������e���,�      �   ;   x���  ���0& �ø�V>���r�M%L,\Zp�z�8&('���>h�4��af��	�      �   .   x���  �w�Dv9���:�,ٲL�Utn������W����$�      �   2   x�3�,N�I�-J-�/*Q�N##]C �4����54�56����� 5�
t      �   �   x��ѽ� ���x�{?g�L�]]`�Bi�h}{�M�f��_��c�U��`r2Hz�'�}%mSW�?2�5��I�Qd��Bz"\B!���A�G���!��G�����1�$
�VR3�R��vp��l�^��ĝ���4�?��bFZ`aьԳ-�g�}�{�       �   k   x��ͱ
�@����J&ɮ��A�8��;�N�e��c�FX,0�Dy���:��t��E3Y9��7��FV��1��=>乫G�eis^Y`��r�v)]-�*s5&     