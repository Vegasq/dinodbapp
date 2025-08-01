# Data Models

Understanding DinoDB's data structures and organization.

## Account Model

### Account Properties
Each AWS account in DinoDB contains:

- **Name**: Descriptive account identifier
- **Region**: AWS region (e.g., us-east-1, us-west-2)
- **Description**: Optional account description
- **Tags**: Organizational labels for categorization
- **Created Date**: When the account was added to DinoDB

### Account Types
DinoDB supports two types of accounts:

#### Stored Accounts
- Saved directly in DinoDB
- Credentials stored securely in macOS Keychain
- Full editing capabilities
- Custom metadata support

#### AWS Profile Accounts
- Read from `~/.aws/credentials` file
- Read-only access
- Automatically synchronized
- Marked with document icon

## Table Information

### Table Metadata
DinoDB displays comprehensive table information:

- **Table Name**: DynamoDB table identifier
- **Item Count**: Approximate number of items
- **Table Size**: Storage size in bytes
- **Key Schema**: Partition and sort key definitions
- **Provisioned Throughput**: Read/write capacity settings
- **Global Secondary Indexes**: Additional query patterns
- **Local Secondary Indexes**: Alternative sort key options

### Table Status
- **Active**: Table is available for operations
- **Creating**: Table is being created
- **Updating**: Table modification in progress
- **Deleting**: Table deletion in progress

## Item Structure

### DynamoDB Item Format
Items in DynamoDB use a specific attribute-value format:

```json
{
  "id": {"S": "user123"},
  "name": {"S": "John Doe"},
  "age": {"N": "30"},
  "active": {"BOOL": true},
  "tags": {"SS": ["premium", "verified"]}
}
```

### Attribute Types
DinoDB supports all DynamoDB attribute types:

- **S**: String
- **N**: Number
- **B**: Binary
- **SS**: String Set
- **NS**: Number Set
- **BS**: Binary Set
- **M**: Map (nested object)
- **L**: List (array)
- **NULL**: Null value
- **BOOL**: Boolean

## Query Parameters

### Query Configuration
When building queries, you can specify:

- **Partition Key**: Required equality condition
- **Sort Key**: Optional range or equality condition
- **Filter Expression**: Additional item filtering
- **Projection Expression**: Specific attributes to return
- **Index Name**: Global or Local Secondary Index
- **Limit**: Maximum items to return
- **Scan Forward**: Sort order for results

### Pagination
DinoDB handles large result sets through:

- **Page Size**: Configurable items per page
- **Last Evaluated Key**: Continuation token
- **Total Count**: Estimated total items
- **Page Navigation**: Forward/backward controls

*This documentation describes the data structures users work with in DinoDB*