# Week 4 — SQL Databases

In the fourth week, we will harness the power of Structured Query Language. This advanced database will serve as the repository for user profiles, seamlessly integrating their platform activities, which encompass Create, Read, Update, and Delete operations. 

Through this exploration, we aspire to deepen our understanding of how databases intricately manage user interactions, thereby augmenting our practical skill set in a significant manner.

## Week Four Main Tasks
- [Week 4 — SQL Databases](#week-4--sql-databases)
  - [Opting for PostgreSQL](#opting-for-postgresql)
    - [Pathways to Success in Database](#pathways-to-success-in-database)
  - [Amazon Relational Database Service](#amazon-relational-database-service)
    - [Creating an RDS Instance in AWS Console](#creating-an-rds-instance-in-aws-console)
    - [Creating an RDS Instance in AWS CLI](#creating-an-rds-instance-in-aws-cli)
  - [PSQL for Everyone](#psql-for-everyone)
    - [SQL Maestro Pro](#sql-maestro-pro)
  - [Cruddur Database Create](#cruddur-database-create)
  - [Design PSQL Schema](#design-psql-schema)
    - [Step 1 : PostgreSQL UUID](#step-1--postgresql-uuid)
    - [Step 2 : Load Intial PSQL Schema](#step-2--load-intial-psql-schema)
    - [Step 3: Expand Dropping Tables](#step-3-expand-dropping-tables)
    - [Step 4: Creating the `users` Table](#step-4-creating-the-users-table)
    - [Step 5: Creating the `activities` Table](#step-5-creating-the-activities-table)
    - [Step 6: Schema Successfully Established](#step-6-schema-successfully-established)
    - [Step 7: RELOAD SQL Schema](#step-7-reload-sql-schema)
  - [Simplify Connecting To PSQL](#simplify-connecting-to-psql)
  - [Connecting to AWS RDS Instance in Gitpod](#connecting-to-aws-rds-instance-in-gitpod)
    - [Step 1: Set Environment Variable](#step-1-set-environment-variable)
    - [Step 2: Adjust Security Group Inbound Rules](#step-2-adjust-security-group-inbound-rules)
    - [Step 3: Test Database Connection](#step-3-test-database-connection)
    - [Step 4: Security Group Update](#step-4-security-group-update)
    - [Step 5: Automate Security Group Update](#step-5-automate-security-group-update)
    - [Step 6: Load Schema to RDS](#step-6-load-schema-to-rds)
    - [Step 7: Test Prod Connection and Schema](#step-7-test-prod-connection-and-schema)
  - [Bash Scripts for Database Operations](#bash-scripts-for-database-operations)
    - [Step 1: Organize Script Files](#step-1-organize-script-files)
    - [Step 2: Add Shebang and Permissions](#step-2-add-shebang-and-permissions)
    - [Step 3: Implement Database Operation Scripts](#step-3-implement-database-operation-scripts)
    - [Step 4: Synergizing Scripts for Speed](#step-4-synergizing-scripts-for-speed)
    - [Bonus: Aesthetics in Bash Scripts](#bonus-aesthetics-in-bash-scripts)

## Opting for PostgreSQL

![PostgreSQL Top Pick](assets/week4/lq-w4-banner.png)

PostgreSQL is a top database engine in the market for a reason. It offers a wide range of powerful features, it is reliable and robust, and it has a large and active community of users and developers.

```mermaid
pie title Core PSQL Features
"Advanced Features" : 40
"Robustness and Reliability" : 35
"Community Support" : 20
"Extensibility" : 25
"Standards Compliance" : 30
```

* **Open source and free:** It is freely available to use, modify, and distribute.
* **ACID compliance:** PostgreSQL guarantees that all transactions are atomic, consistent, isolated, and durable.
* **JSON and XML support:** The engine supports the JSON and XML data types, which makes it a good choice for applications that need to store and query semi-structured data.
* **Full-text search:** PostgreSQL has built-in full-text search capabilities, which makes it easy to find data within large datasets.
* **Replication and clustering:** PostgreSQL supports replication and clustering, which makes it possible to scale the database to meet the needs of growing applications.

**Our** initial steps will involve creating the database, establishing a connection to it, and subsequently outlining a schema that aligns with the specifications mentioned earlier.

### Pathways to Success in Database
I am surpassing my initial expectations with this section, and I am creating a clear path for you, driven by my affection towards you.

DBAs are more concerned with the technical aspects of database management and maintenance, while Data Analysts focus on extracting meaningful insights from the data for decision-making purposes.

[Create a Diagram Like This One.](resources/mermaid.md)

```mermaid
journey
  title Database Management Office Hours
  section Designing Tables
    Define schema: 5: DBA
    Create indexes: 3: DBA
    Optimize queries: 1: DBA, Analyst
  section Data Manipulation
    Insert records: 5: DBA
    Update entries: 3: DBA
    Analyze data: 1: Analyst
  section Maintenance
    Backup data: 5: DBA
    Monitor performance: 3: DBA
    Fine-tune system: 2: DBA
```

If you possess a keen interest in the realm of data, I recommend embarking on a trajectory that starts with assuming the role of a **Data Analyst** and subsequently progressing through the ranks to eventually become a **Data Administrator**, Engineer, and ultimately an Architect.

| Role                     | Responsibilities                                                                                     |
|--------------------------:|:-------------------------------------------------------------------------------------------------------|
| Data Analyst             | **Data Manipulation**<br>► Analyze Data: Extract insights and patterns using SQL and analysis tools.   |
| Database Administrator   | **Designing Tables**<br>► Define Schema: Design efficient database schema with tables and relationships.<br><br>**Data Manipulation**<br>► Insert Records: Ensure data integrity during record insertion.<br>► Update Entries: Enforce data constraints during updates.<br><br>**Optimizing Queries:**<br>► Optimize Queries: Enhance query performance using indexes and analysis.<br><br>**Maintenance:**<br>► Backup Data: Perform data backups for recovery.<br>► Monitor Performance: Identify and resolve performance issues.<br>► Fine-Tune System: Optimize system resources. |
| Data Engineer            | **Data Management**<br>► ETL Processes: Develop and manage Extract, Transform, Load (ETL) processes.<br>► Data Integration: Integrate data from various sources into cohesive pipelines.<br><br>**Infrastructure**<br>► Data Storage: Design and manage data storage solutions.<br>► Data Transformation: Develop data transformation logic for analysis and reporting.<br><br>**Data Quality:**<br>► Data Cleansing: Ensure data quality and consistency.<br>► Data Pipeline Monitoring: Monitor data flows for accuracy and reliability. |
| Data Architect           | **System Design**<br>► Architect Data Solutions: Design scalable and efficient data architecture.<br>► Data Modeling: Create advanced data models for complex business needs.<br><br>**Leadership**<br>► Team Collaboration: Lead data teams, aligning efforts with business objectives.<br>► Technology Selection: Evaluate and select appropriate data technologies

You can follow the path I outlined, founded on trust and practical expertise. Drawing from my firsthand experience in working with data and effectively leveraging Google Cloud, Azure, and AWS services for substantial big data and machine learning projects, you can have full confidence in the credibility of this roadmap.

Each role builds upon the previous, culminating in an enriching journey marked by both personal growth and impactful contributions to the world of data management and analysis.


| 💡  | I can direct you towards a range of tech, Incl. Amazon Redshift, BigQuery, and [Google Looker](assets/week4/poc/looker-for-data.png).     |
|---------------|:------------------------|


## Amazon Relational Database Service
RDS is a cutting-edge cloud-based solution that has revolutionized the way databases are managed and hosted. 

RDS offers a seamless and efficient way to host, manage, and scale relational databases like PostgreSQL without the need for extensive infrastructure management. We'll integrate this database to facilitate CRUD operations, enabling us to store user posts seamlessly. 

### Creating an RDS Instance in AWS Console
Navigate to the console for further insights into the workings of RDS.
1. Go to the RDS section in the AWS Management Console.
2. Click the `"Create database"` button.
3. Choose `"Standard Create"` and select the `PostgreSQL` engine.
4. Specify a unique identifier for your DB instance.
5. Configure instance details, such as class, storage, and VPC settings.
6. Set a secure master username and password.
7. Configure network settings and enable `"Publicly accessible"`.
8. Provide a database name and choose a port.
9. Enable `Performance Insights` and set a retention period.
10. Set backup retention to `0` and disable deletion protection.
11. Choose storage type and enable encryption.
12. Review and create the instance.

<img src="assets/week4/1-ProdDB/3 anyway bro.png">

- Monitor creation progress on the RDS Dashboard.

```
DB instance created:
Instance ID: `cruddur-db-instance`
Engine: `PostgreSQL`
Instance Class: `db.t3.micro`
...
Status: `Creating`
```
<img src="assets/week4/1-ProdDB/9 overviw rds itruns ontop of ec2.png">

### Creating an RDS Instance in AWS CLI
The preceding clicks were meticulously crafted within a solitary command-line prompt, encompassing all operations within distinct flags with [this synopsis.](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html)

<img src="assets/week4/1-ProdDB/6 done.png">

- Duplicate the provided CLI command and carefully examine the required areas.

```
aws rds create-db-instance \
  --db-instance-identifier cruddur-db-instance \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --engine-version  14.6 \
  --master-username <required> \
  --master-user-password <required> \
  --allocated-storage 20 \
  --availability-zone <required> \
  --backup-retention-period 0 \
  --port 5432 \
  --no-multi-az \
  --db-name cruddur \
  --storage-type gp2 \
  --publicly-accessible \
  --storage-encrypted \
  --enable-performance-insights \
  --performance-insights-retention-period 7 \
  --no-deletion-protection
```

#### Required
- Choose a `master-username`
- `master-user-password` with a length between 8 and 30 characters.
- Change `availability-zone` with yours

| ⛔ | RDS operates on EC2 and can only undergo a temporary suspension for up to seven days.  Beyond this period, it will automatically resume. |
|:-----:|-------------|
| 💡    | Proceed with a momentary halt of the RDS instance and remember to establish a notification for its automatic restart in seven days. |

- Access AWS RDS, navigate to the "Databases" section, and select the desired database entry.


<img src="assets/week4/1-ProdDB/8 db ready.png">

Please await the RDS status to transition to the "Available" stated by the green indicator.

#### Considerations
**5432** is the default port used by PostgreSQL. Many attackers will scan for databases on the default port, so changing it might reduce the number of automated attacks targeting your database.

## PSQL for Everyone

In this segment, I will make every effort to equip you with SQL knowledge. We are going to initiate our local PostgreSQL instance and establish a connection to it.

- Earlier (Week-1), we set up psql as a container, and I walked you through the procedure [right here](week1.md#postgresql-container).

Now, we will demonstrate how to simply execute that.

1. Run the following command in a terminal:
```
docker compose up
```
2. Connect with the password `password`.
```bash
gitpod /workspace/aws-cloud-project-bootcamp (main) $ psql -Upostgres -h localhost
```

<img src="assets/week4/2- localwork/2 opla we are back.png">

### SQL Maestro Pro

The array of tasks and activities that can be accomplished within the realm of database management is remarkably extensive.
1. To start off, initiate the process by creating your own database, for instance;
```sql
CREATE DATABASE database_name; 
```
2. Discard the database if it's no longer required.
```sql
DROP DATABASE database_name;
```
<img src="assets/week4/2- localwork/18 db drop done ofc pro.png">

3. Additionally, you can execute straightforward tasks such as;

| Command                | Description                                                  | Example |
|------------------------|--------------------------------------------------------------|---------|
| `\x`                   | Enable expanded display when viewing data.                  | `\x on` |
| `\q`                   | Quit the PSQL command-line interface.                       | `\q`    |
| `\l`                   | List all available databases.                               | `\l`    |
| `\c database_name`     | Connect to a specific database.                             | `\c database_name` |
| `\dt`                  | List all tables in the current database.                   | `\dt`   |
| `\d table_name`        | Describe a specific table's structure.                      | `\d table_name` |
| `\du`                  | List all users and their roles.                             | `\du`   |
| `\dn`                  | List all schemas in the current database.                   | `\dn`   |

<details>

<summary>
4. Moreover, you can delve into more sophisticated operations <b> inside.</b>
</summary>
  
| Command         | Description                                                                                              | Example SQL                                   |
|-----------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| SELECT          | Retrieve data from a database.                                                                          | `SELECT column1, column2 FROM table_name;`    |
| INSERT          | Add new records into a table.                                                                           | `INSERT INTO table_name (column1, column2) VALUES (value1, value2);` |
| UPDATE          | Modify existing records in a table.                                                                     | `UPDATE table_name SET column1 = value1 WHERE condition;` |
| DELETE          | Remove records from a table.                                                                            | `DELETE FROM table_name WHERE condition;`     |
| CREATE TABLE    | Create a new table in the database.                                                                     | ```sql CREATE TABLE table_name ( column1 datatype, column2 datatype, ... ); ``` |
| ALTER TABLE     | Modify an existing table (add, modify, or delete columns).                                            | ```sql ALTER TABLE table_name ADD column_name datatype; ```<br> ```sql ALTER TABLE table_name MODIFY column_name datatype; ```<br> ```sql ALTER TABLE table_name DROP COLUMN column_name; ``` |
| DROP TABLE      | Delete a table and its data.                                                                            | `DROP TABLE table_name;`                     |
| CREATE INDEX    | Create an index on columns to improve query performance.                                               | `CREATE INDEX index_name ON table_name (column_name);` |
| ALTER INDEX     | Modify an existing index.                                                                               | `ALTER INDEX index_name REBUILD;`            |
| JOIN            | Combine rows from multiple tables based on related columns.                                           | `SELECT column1, column2 FROM table1 INNER JOIN table2 ON table1.column = table2.column;` |
| GROUP BY        | Group rows with the same values in specified columns.                                                 | `SELECT column1, COUNT(*) FROM table_name GROUP BY column1;` |
| HAVING          | Filter results of aggregate functions in combination with GROUP BY.                                  | `SELECT column1, COUNT(*) FROM table_name GROUP BY column1 HAVING COUNT(*) > 5;` |
| ORDER BY        | Sort the result set by one or more columns.                                                           | `SELECT column1, column2 FROM table_name ORDER BY column1 ASC, column2 DESC;` |
| UNION           | Combine result sets of multiple SELECT statements (removes duplicates).                              | `SELECT column1 FROM table1 UNION SELECT column1 FROM table2;` |
| UNION ALL       | Similar to UNION, but includes duplicate rows.                                                        | `SELECT column1 FROM table1 UNION ALL SELECT column1 FROM table2;` |

I'm new Yaya! Sure [check this](https://www.w3schools.com/sql/sql_syntax.asp)

</details>


## Cruddur Database Create
1. To get started, simply prepare your databse by creating one.

```sql
CREATE database cruddur;
```
2. Inside the psql shell, run `\l` to list DBs.
```bash
List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 cruddur   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
```

<img src="assets/week4/2- localwork/4 create db.png">

To establish the foundational SQL structure the database we require an **SQL file that defines its schema**.

## Design PSQL Schema
While many web frameworks include a `schema.sql` file for the purpose of defining database tables during database creation, Flask, on the other hand, requires the manual creation of this file.

```mermaid
graph TD
    A[Users] -->|1| B[Activities]
    B -->|n| C[Comments]
    B -->|1| D[Tags]
    A -->|1..n| E[Profile]
```

A `schema.sql` file is a script or a set of instructions written in SQL (Structured Query Language) that outlines the structure and organization of a database. In this file, you define the `tables`, their `columns`, data `types`, `constraints`, `relationships`, and other relevant database `elements`.

**Step Zero :** In `backend-flask/db`, create a `schema.sql` file.
- [Step 1 : PostgreSQL UUID](#step-1--postgresql-uuid)
- [Step 2 : Load Intial PSQL Schema](#step-2--load-intial-psql-schema)
- [Step 3 : Expand Dropping Tables](#step-3-expand-dropping-tables)
- [Step 4 : Creating the `users` Table](#step-4-creating-the-users-table)
- [Step 5 : Creating the `activities` Table](#step-5-creating-the-activities-table)
- [Step 6 : Schema Successfully Established](#step-6-schema-successfully-established)
- [Step 7 : RELOAD SQL Schema ](#step-7-reload-sql-schema)


### Step 1 : PostgreSQL UUID
Include the following line within the file to enable the UUID extension for PostgreSQL.
```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

We'll use `uuid-ossp` to enable PostgreSQL to generate UUIDs.

|💡      |UUIDs enhances uniqueness and reduces the likelihood of ID collisions when compared to numeric IDs.      |
|---------------|:------------------------|


### Step 2 : Load Intial PSQL Schema

1. **Quit `psql`:** If you have a psql session open, close it by typing the command:
```psql
\q
```
This will exit the current `psql` session.

2. **Load schema.sql**: Navigate to the `backend` folder in your project directory and run the following command:
```bash
psql cruddur < db/schema.sql -h localhost -U postgres
```
- `psql`: This is the **PostgreSQL command line tool** used to interact with the PostgreSQL database server.
- `cruddur`: This is the **name of the database** you want to connect to.
- `< db/schema.sql`: This indicates that you want to input the **contents of the `schema.sql` file** into the `psql` command.
- `-h localhost`: This specifies the **host** (in this case, your local machine).
- `-U postgres`: This specifies the **PostgreSQL username** to use (in this case, "postgres").

3. **Password Prompt:** When you run the command, you'll be prompted to enter the password for the "postgres" user. Enter the correct password associated with the "postgres" user.

4. **Terminal Output:** If the schema file is loaded successfully, you'll see output analogous to the one I had:

 ```
$ psql cruddur < db/schema.sql -h localhost -U postgres
Password for user postgres: 

CREATE EXTENSION 
 ```

<img src="assets/week4/2- localwork/6 executing extension.png">

This output indicates that the commands in the `schema.sql` have been executed, including creating extension.

### Step 3: Expand Dropping Tables
Start by dropping two tables `public.users` and `public.activities` if they already exist in the database. This ensures that any previous versions of these tables are removed before creating new ones.
```sql
DROP TABLE IF EXISTS public.users;
DROP TABLE IF EXISTS public.activities;
```
The `DROP TABLE IF EXISTS` statement is used to delete the specified table if it exists. The public in `public.users` and `public.activities` indicates the schema where the tables are located.

### Step 4: Creating the `users` Table
Create a new table called `users` in the public schema. This table will store information about users.
```sql
CREATE TABLE public.users (
  uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  display_name text NOT NULL,
  handle text NOT NULL,
  email text NOT NULL,
  cognito_user_id text NOT NULL,
  created_at TIMESTAMP default current_timestamp NOT NULL
);
```
Here's a breakdown of the columns in the users table
- **uuid**: A `UUID` (Universally Unique Identifier) column with a default value generated using `uuid_generate_v4()`. This column is set as the primary key of the table.
- **display_name**: A `text` column that stores the display name of the user. It cannot be `NULL` (i.e., it's a required field).
- **handle**: A `text` column that stores a handle or username for the user. It cannot be `NULL`.
- **email**: A `text` column that stores the email address of the user. It cannot be `NULL`.
- **cognito_user_id**: A `text` column that stores an identifier associated with the user in Amazon Cognito (a service for managing user identities). It cannot be `NULL`.
- **created_at**: A `TIMESTAMP` column that stores the timestamp of when the user record was created. It has a default value of the current timestamp and cannot be `NULL`.

### Step 5: Creating the `activities` Table

Create a table called activities in the public schema. This table will store information about various activities.
```SQL
CREATE TABLE public.activities (
  uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_uuid UUID NOT NULL,
  message text NOT NULL,
  replies_count integer DEFAULT 0,
  reposts_count integer DEFAULT 0,
  likes_count integer DEFAULT 0,
  reply_to_activity_uuid integer,
  expires_at TIMESTAMP,
  created_at TIMESTAMP default current_timestamp NOT NULL
);
```
- **uuid**: A `UUID` column with a default value generated using `uuid_generate_v4()`. This column is set as the primary key of the table.
- **user_uuid**: A `UUID` column that stores the UUID of the user associated with the activity. It cannot be `NULL`.
- **message**: A `text` column that stores the message or content of the activity. It cannot be `NULL`.
- **replies_count**, **reposts_count**, **likes_count**: Integer columns that store the counts of replies, reposts, and likes for the activity, respectively. They have default values of 0.
- **reply_to_activity_uuid**: An `integer` column that stores the ID of the activity to which this activity is a reply. It allows for creating a hierarchical structure of activities.
- **expires_at**: A `TIMESTAMP` column that stores the expiration timestamp of the activity (if applicable).
- **created_at**: A `TIMESTAMP` column that stores the timestamp of when the activity record was created. It has a default value of the current timestamp and cannot be `NULL`.

<img src="assets/week4/2- localwork/31 create table and explicit public for microservice later for efverydomain.png">

### Step 6: Schema Successfully Established
Review your design, Mr. Database Architect, and ensure its alignment with the following structure and adequately meets your business requirements.

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

DROP TABLE IF EXISTS public.users;
CREATE TABLE public.users (
  uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  display_name text NOT NULL,
  handle text NOT NULL,
  email text NOT NULL,
  cognito_user_id text NOT NULL,
  created_at TIMESTAMP default current_timestamp NOT NULL
);

DROP TABLE IF EXISTS public.activities;
CREATE TABLE public.activities (
  uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  user_uuid UUID NOT NULL,
  message text NOT NULL,
  replies_count integer DEFAULT 0,
  reposts_count integer DEFAULT 0,
  likes_count integer DEFAULT 0,
  reply_to_activity_uuid integer,
  expires_at TIMESTAMP,
  created_at TIMESTAMP default current_timestamp NOT NULL
);
```

Schema is like the excel file, tables /views are like the sheets in it.

### Step 7: RELOAD SQL Schema 

Once we have successfully refined our schema, it's time to reload it along with the newly created tables for activities and users.

- **Load `schema.sql`**: run the following command again
```bash
psql cruddur < db/schema.sql -h localhost -U postgres
```

<img src="assets/week4/2- localwork/20 schema done.png">

Now you have the `public.users` and `public.activities` tables ready to store data for your application along the previously loaded extension.


## Simplify Connecting To PSQL
In here, we will allocate PostgreSQL development and production connection URLs to environment variables, simplifying the process of connecting to the specific workspace you require in a more efficient manner.

**Local PostgreSQL**
1. Compose the following code to establish a connection with your database:
```bash
psql "postgresql://postgres:password@localhost:5432/cruddur"
```

2. Export the PostgreSQL connection URL as an environment variable. 
```bash
export CONNECTION_URL="postgresql://postgres:password@localhost:5432/cruddur"
```
This will not only simplify the connection process through the environment variable but also enhance the convenience of utilizing it in our upcoming scripts.

3. Persist the variable for future Gitpod workspaces.

```bash
gp env CONNECTION_URL="postgresql://postgres:password@localhost:5432/cruddur"
```

4. Run the following command to examine the connectivity URL

<img src="assets/week4/2- localwork/8 co url done.png">

```bash
psql $CONNECTION_URL
```

**Production PostgreSQL**<br>
Following the approach employed earlier, we will once again incorporate the URL from the RDS instance we established at the outset.

- Set and presist the connection URL for the production RDS DB;

```bash
export PROD_CONNECTION_URL="postgresql://cruddurroot:<password>@<DB_endpoint>:5432/cruddur"

gp env PROD_CONNECTION_URL="postgresql://cruddurroot:<password>@<DB_endpoint>:5432/cruddur"
```

<img src="assets/week4/2- localwork/9 set up prod connection.png">


## Connecting to AWS RDS Instance in Gitpod

Try running the following to connect to prod.
```
psql $PROD_CONNECTION_URL
```
The command will hang indefinitely because the default security group on our RDS instance is configured to allow inbound access exclusively from the security group itself, preventing any external connections.

Get ready for the complete solution.
- [Step 1: Set Environment Variable](#step-1-set-environment-variable)
- [Step 2: Adjust Security Group Inbound Rules](#step-2-adjust-security-group-inbound-rules)
- [Step 3: Test Database Connection](#step-3-test-database-connection)
- [Step 4: Security Group Update](#step-4-security-group-update)
- [Step 5: Automate Security Group Update](#step-5-automate-security-group-update)
- [Step 6: Load Schema to RDS](#step-6-load-schema-to-rds)
- [Step 7: Test Prod Connection and Schema](#step-7-test-prod-connection-and-schema)

### Step 1: Set Environment Variable
In your GitPod environment, i you haven't already, set the `PROD_CONNECTION_URL` environment variable in the following format:
```sh
export PROD_CONNECTION_URL="postgresql://<user>:<password>@<RDS endpoint>:5432/<master database name>"
gp env PROD_CONNECTION_URL="postgresql://<user>:<password>@<RDS endpoint>:5432/<master database name>"
```

### Step 2: Adjust Security Group Inbound Rules

1. Connect to your AWS RDS console.
2. Adjust the security group inbound rules to allow Gitpod's IP address to connect to your database.
3. Get the Gitpod IP address using the command:
```sh
GITPOD_IP=$(curl ifconfig.me)
```
4. Add an inbound rule to the RDS security group for the Gitpod IP address (`$GITPOD_IP`).

### Step 3: Test Database Connection
1. Run the command:
```sh
psql $PROD_CONNECTION_URL
```
2.  Run the `\l` command to list prod databases.

<img src="assets/week4/5- Establish RDS-Connection/27 listing rds db.png">

The existing configuration requires us to manually update the IP address each time.

### Step 4: Security Group Update

1. Set environment variables for the security group and the inbound rule:

```sh
export DB_SG_ID="<security-group-id>"
export DB_SG_RULE_ID="<security-group-rule-id>"

gp env DB_SG_ID="<security-group-id>"
gp env DB_SG_RULE_ID="<security-group-rule-id>"
```
- Use `DB_SG_ID` to refer to the ID of the security group itself.
- Use `DB_SG_RULE_ID` for the unique identifier of the inbound rule we've configured in the security group.

2. Use the following CLI script to update the security group rule with the Gitpod IP address:
```sh
aws ec2 modify-security-group-rules \
    --group-id $DB_SG_ID \
    --security-group-rules "SecurityGroupRuleId=$DB_SG_RULE_ID,SecurityGroupRule={Description=GITPOD,IpProtocol=tcp,FromPort=5432,ToPort=5432,CidrIpv4=$GITPOD_IP/32}"
```
3. Verify it returns the following

<img src="assets/week4/5- Establish RDS-Connection/AutomateRDSrules/7 added description ofc.png">

```
{
    "Return": true
}
```
4. Verify the ip is updated in the console

<img src="assets/week4/5- Establish RDS-Connection/AutomateRDSrules/6 hey applied perfect ready to include it in a script.png">

### Step 5: Automate Security Group Update
1. Create a file named `rds-update-sg-rule` inside the `/bin` with the following content:
```sh
#! /usr/bin/bash

aws ec2 modify-security-group-rules \
    --group-id $DB_SG_ID \
    --security-group-rules "SecurityGroupRuleId=$DB_SG_RULE_ID,SecurityGroupRule={Description=GITPOD,IpProtocol=tcp,FromPort=5432,ToPort=5432,CidrIpv4=$GITPOD_IP/32}"
```
<img src="assets/week4/5- Establish RDS-Connection/AutomateRDSrules/9 making the script and makin it exe the up rds sg rule.png">

2. Make the script executable:
```
chmod u+x rds-update-sg-rule
```
<img src="assets/week4/5- Establish RDS-Connection/AutomateRDSrules/11 applied the script.png">


3. Update `.gitpod.yml` to run the script on environment startup part of postgre setup:
```yaml
- name: postgres
  init: |
      # check the file.
  command: |
    export GITPOD_IP=$(curl ifconfig.me)
    source "$THEIA_WORKSPACE_ROOT/backend-flask/bin/rds-update-sg-rule"
```

<img src="assets/week4/5- Establish RDS-Connection/AutomateRDSrules/13 making it a requirement in every init gitpo.png">

### Step 6: Load Schema to RDS
1. Update the Docker Compose connection URL to the production URL in `docker-compose.yml`:
```
CONNECTION_URL: "${PROD_CONNECTION_URL}"
```
2. Run the `db-schema-load` script in production:
```
./backend-flask/bin/db-schema-load prod
```

### Step 7: Test Prod Connection and Schema
1. Update `./bin/db-connect` to include a condition for the 'prod' parameter.
2. Test connectivity to the production database by running the script.
```
./bin/db-connect prod
```
```bash
bin/db-connect prod
running in production
psql (13.10 (Ubuntu 13.10-1.pgdg22.04+1), server 14.6)
WARNING: psql major version 13, server major version 14.
         Some psql features might not work.
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

cruddur=>
```

## Bash Scripts for Database Operations

In this comprehensive instructional guide, we will walk you through the process of setting up a series of bash scripts to manage various database operations, such as creating and dropping databases, loading schemas, and seeding data. 

This week initiates the launch of the much-awaited bin directory's construction. This organized workflow will enhance your efficiency and maintainability while working with databases.

```bash
./bin
├── db-create
├── db-drop
├── db-connect
├── db-sessions
├── db-setup
├── db-seed
├── db-schema-load
└── db-rds-update-sg-rule
```

These scripts will be relocated to bin/db ([Week Six](week6.md)), attributed to the implementation of diverse technological scripts in a proactive development approach. 

- [Step 1: Organize Script Files](#step-1-organize-script-files)
- [Step 2: Add Shebang and Permissions](#step-2-add-shebang-and-permissions)
- [Step 3: Implement Database Operation Scripts](#step-3-implement-database-operation-scripts)
- [Step 4: Synergizing Scripts for Speed](#step-4-synergizing-scripts-for-speed)
- [Bonus: Aesthetics in Bash Scripts](#bonus-aesthetics-in-bash-scripts)

### Step 1: Organize Script Files

1. Begin by creating a new directory called bin within your backend project's root directory. This directory will house all your bash scripts related to database operations.
```
mkdir bin
```
2. Inside the bin directory, create the file structure provided.
```sh
touch bin/db-create
touch bin/db-drop
touch bin/db-connect
touch bin/db-connections
touch bin/db-setup
touch bin/db-seed
touch bin/db-schema-load
touch bin/db-rds-update-sg-rule
```
Benefits of naming scripts without extensions Inlc. **Clear Intent, Portability, File Type Agnostic and looks *n*ice**.

### Step 2: Add Shebang and Permissions
1. For each script file, add the shebang line at the top to indicate that the script should be executed with Bash.
```sh
#! /usr/bin/bash
```
<img src="assets/week4/2- localwork/10 continue with db treate this files as bash scripts.png">

2. Make all the script files executable by running the following command for each file:
```sh
chmod u+x bin/<filename>
```
3. You can apply to all the bin directory in one command to all files:
```sh
chmod -R u+x bin/
```

<img src="assets/week4/2- localwork/13 exec not just for user but all of em incl groups.png">

### Step 3: Implement Database Operation Scripts

1. Develop `db-create` script
```sh
#! /usr/bin/bash

NO_DB_CONNECTION=$(sed 's/\/cruddur//g' <<< "$CONNECTION_URL")
psql $NO_DB_CONNECTION -c "create database cruddur;"
```
- `First`: Uses the `sed` command to extract a modified version of the `CONNECTION_URL`. This modified URL removes the trailing "/cruddur" segment from the connection URL. The modified URL is stored in the `NO_DB_CONNECTION` variable.
- `Second`: Executes the `psql` command to create a new database named "cruddur" using the modified connection URL stored in the `NO_DB_CONNECTION` variable. The `-c` flag specifies a command to be executed within `psql`.

```SQL
sed 's/\/cruddur//g'
```
To get rid of `/` do `\` infront of it

for this `/cruddur//` It will take it and change it with empty using `//`

Now let's feed it to our connection string:

```SQL
sed 's/\/cruddur//g' <<< "$CONNECTION_URL"
```

WRAPPING in dollar sign so we can assign it to our env var

```SQL
NO_DB_CONNECTION=$(sed 's/\/cruddur//g' <<< "$CONNECTION_URL"
```

2. Develop `db-drop` script
```sh
#! /usr/bin/bash

NO_DB_CONNECTION_URL=$(sed 's/\/cruddur//g' <<<"$CONNECTION_URL")
psql $NO_DB_CONNECTION_URL -c "drop database IF EXISTS cruddur;"
```
- `First`: Modify `CONNECTION_URL` to remove "/cruddur" segment, store in `NO_DB_CONNECTION_URL`.
- `Second`: Drop database "cruddur" using modified URL, if exists.

3. Develop `db-connect` script
```sh
#! /usr/bin/bash

if [ "$1" = "prod" ]; then
  echo "using production"
  URL=$PRODUCTION_URL
else
  URL=$CONNECTION_URL
fi

psql $URL
```
   - Determine connection URL based on argument:
     - If argument is "prod," use production URL.
     - Otherwise, use default connection URL.
   - Use the determined URL to connect using `psql`.
4. Develop `db-sessions` script
```sh
#! /usr/bin/bash


if [ "$1" = "prod" ]; then
  echo "using production"
  CONNECTION_URL=$PROD_CONNECTION_URL
else
  CONNECTION_URL=$CONNECTION_URL
fi

NO_DB_URL=$(sed 's/\/cruddur//g' <<<"$CONNECTION_URL")
psql $NO_DB_URL -c "select pid as process_id, \
       usename as user,  \
       datname as db, \
       client_addr, \
       application_name as app,\
       state \
from pg_stat_activity;"
```
- Determine connection URL based on argument:
  - If argument is "prod," use production connection URL.
  - Otherwise, use default connection URL.
- Modify the determined connection URL, store in `NO_DB_URL`.
- Use `psql` to execute a SQL query that retrieves process information from the PostgreSQL `pg_stat_activity` view.

5. Develop `seed.sql` for the testing data.

```bash
./backend-flask/
│
└── sql/
    └── seed.sql
```
```SQL
```sql
-- this file was manually created

INSERT INTO
    public.users (
        display_name,
        handle,
        cognito_user_id
    )
VALUES  (
        'Yahya Abulhaj',
        'yaya2devops',
        'MOCK'
    );

INSERT INTO
    public.activities (user_uuid, message, expires_at)
VALUES ( (
            SELECT uuid
            from public.users
            WHERE
                users.handle = 'yaya2devops'
            LIMIT
                1
        ), 'This was imported as seed data!', current_timestamp + interval '10 day'
    )
```
6. Develop `db-seed` script to seed the above.
```sh
#! /usr/bin/bash

ABS_PATH=$(readlink -f "$0")
DB_PATH=$(dirname $ABS_PATH)
BIN_PATH=$(dirname $DB_PATH)
PROJECT_PATH=$(dirname $BIN_PATH)
BACKEND_FLASK_PATH="$PROJECT_PATH/backend-flask"
seed_path="$BACKEND_FLASK_PATH/db/seed.sql"
echo $seed_path

if [ "$1" = "prod" ]; then
  echo "using production"
  CONNECTION_URL=$PRODUCTION_URL
else
  CONNECTION_URL=$CONNECTION_URL
fi

psql $CONNECTION_URL cruddur < $seed_path
```
- Get script's absolute path, store in `ABS_PATH`.
- Derive script's directory path, store in `DB_PATH`.
- Derive bin directory path, store in `BIN_PATH`.
- Derive project directory path, store in `PROJECT_PATH`.
- Define Flask project path in `BACKEND_FLASK_PATH`.
- Define seed SQL file path in `seed_path`.
- Echo `seed_path` to console.
- Determine connection URL based on provided argument:
  - If `prod,` use production connection URL.
  - Else, use default connection URL.
- Use psql to execute seed SQL file on specified database (cruddur) using determined connection URL.

6. Develop `db-schema-load` script
```sh
#! /usr/bin/bash

ABS_PATH=$(readlink -f "$0")
DB_PATH=$(dirname $ABS_PATH)
BIN_PATH=$(dirname $DB_PATH)
PROJECT_PATH=$(dirname $BIN_PATH)
BACKEND_FLASK_PATH="$PROJECT_PATH/backend-flask"
schema_path="$BACKEND_FLASK_PATH/db/schema.sql"
echo $schema_path

if [ "$1" = "prod" ]; then
  echo "using production"
  CONNECTION_URL=$PRODUCTION_URL
else
  CONNECTION_URL=$CONNECTION_URL
fi


psql $CONNECTION_URL cruddur < $schema_path
```
- Get absolute path as `ABS_PATH`.
- Derive script's directory as `DB_PATH`.
- Define Flask project path as `BACKEND_FLASK_PATH`.
- Determine connection URL based on argument as `CONNECTION_URL`.
- Define schema file path as `schema_path`.
- Echo schema path.
- If argument is "prod," use production URL.
- Use `psql` to apply schema setup using determined URL.

> Refer to the process of [designing the schema for PostgreSQL](#design-psql-schema).

7. Observe `rds-update-sg-rule`, It was used for [this purpose](#step-5-automate-security-group-update).

### Step 4: Synergizing Scripts for Speed

We'll streamline the scripts needed to set up PostgreSQL each time, simplifying the process of configuring psql for future workspaces.

- Develop `db-setup` script
```sh
#! /usr/bin/bash
set -e # stop it if it failed at any stage

ABS_PATH=$(readlink -f "$0")
DB_PATH=$(dirname $ABS_PATH)

source "$DB_PATH/drop"
source "$DB_PATH/create"
source "$DB_PATH/schema-load"
source "$DB_PATH/seed"
python "$DB_PATH/migrate"
python "$DB_PATH/update_cognito_user_ids"
```

This script is designed to automate the process of managing a database. It performs several essential tasks related to the database setup and maintenance.
- `source "$DB_PATH/drop"`: Executes a script to drop an existing database.
- `source "$DB_PATH/create"`: Executes a script to create a new database.
- `source "$DB_PATH/schema-load"`: Executes a script to load the database schema.
- `source "$DB_PATH/seed"`: Executes a script to populate the database with initial data.
- `python "$DB_PATH/migrate"`: Executes a Python script named `migrate` for database migrations.
- `python "$DB_PATH/update_cognito_user_ids"`: Executes a Python script for updating user IDs cognito

### Bonus: Aesthetics in Bash Scripts
Incorporating color into Bash scripts is a way to elevate their visual appeal and clarity. Instead of monotonous plain text, you can add vibrancy using colored outputs. 

To achieve this effect, a combination of escape codes and variables is employed.
```sh
CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="db-schema-load"
printf "${CYAN}== ${LABEL}${NO_COLOR}\n"
```

The above snippet adds color to the scripts using the echo command that uses escape sequences stored in `CYAN` and `NO_COLOR` variables to apply cyan and default colors to text. 

When combined in the printf statement, it creates visually appealing output with `==` in cyan and the label in the default color. 

Here's a table presenting the colors to choose from; 

| Color    | Escape Code   | Example Variable   | Example Usage               |
|----------|---------------|--------------------|-----------------------------|
| Red      | '\033[1;31m' | RED='\033[1;31m' | printf "${RED}Text\${NO_COLOR}\\n" |
| Green    | '\033[1;32m' | GREEN='\033[1;32m' | printf "${GREEN}Text\${NO_COLOR}\\n" |
| Blue     | '\033[1;34m' | BLUE='\033[1;34m' | printf "${BLUE}Text\${NO_COLOR}\\n" |
| Yellow   | '\033[1;33m' | YELLOW='\033[1;33m' | printf "${YELLOW}Text\${NO_COLOR}\\n" |
| Magenta  | '\033[1;35m' | MAGENTA='\033[1;35m' | printf "${MAGENTA}Text\${NO_COLOR}\\n" |
| Cyan     | '\033[1;36m' | CYAN='\033[1;36m' | printf "${CYAN}Text\${NO_COLOR}\\n" |
| Reset    | '\033[0m'    | NO_COLOR='\033[0m' | Reset color to default     |


1. Enhance the visual appeal of the scripts within the step script by applying colors that align with your preferences, such as using red for "drop" and green for "create," and so on.
2. Add this visual to the step script itself
```sh
CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="sqldb-welcome-setup"
printf "${CYAN}==== ${LABEL}${NO_COLOR}\n"
```
3. Execute the step script to experience the visual enhancements in action.

<img src="assets/week4/3- psqlquery/8 all at once.png">

---
*To Be Continued..*
---