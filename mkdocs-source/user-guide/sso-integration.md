# AWS SSO Integration

AWS Single Sign-On (IAM Identity Center) integration is a premium feature available in **DinoDB PRO** that provides enterprise-grade authentication for AWS environments. This feature allows seamless integration with your organization's AWS access portal and eliminates the need to manage individual AWS access keys.

## Overview

AWS SSO integration enables you to:

- **Centralized Authentication**: Use your organization's AWS SSO portal for authentication
- **Multiple Account Access**: Automatically discover all AWS accounts accessible through your SSO configuration
- **Role-Based Access**: Select appropriate IAM roles for each account
- **Secure Token Management**: Automatic token refresh and secure storage in macOS Keychain
- **Session Persistence**: Maintain authentication across app restarts

## Benefits

### Enterprise Security
- **No Access Keys**: Eliminate the need to store long-term AWS access keys
- **Centralized Control**: IT administrators maintain full control over access permissions
- **Audit Trail**: All access is logged through your organization's SSO system
- **Automatic Rotation**: Credentials are automatically rotated and refreshed

### Developer Experience
- **Single Login**: Authenticate once to access all permitted AWS accounts
- **Account Discovery**: Automatically see all available accounts and roles
- **Seamless Switching**: Easily switch between different AWS accounts and roles
- **Modern Authentication**: Uses OAuth 2.0 and OpenID Connect standards

## Prerequisites

Before setting up AWS SSO in DinoDB PRO, ensure:

1. **DinoDB PRO License**: SSO integration is only available with a commercial license
2. **AWS SSO Setup**: Your organization has AWS SSO (IAM Identity Center) configured
3. **SSO Access**: You have been granted access to AWS accounts through SSO
4. **macOS Version**: Running macOS 14.0 or later

## Setting Up AWS SSO

### Step 1: Obtain SSO Configuration Details

You'll need the following information from your AWS administrator:

- **SSO Start URL**: Your organization's AWS access portal URL
  - Format: `https://your-org.awsapps.com/start`
- **SSO Region**: The AWS region where your SSO instance is hosted
  - Common regions: `us-east-1`, `us-west-2`, `eu-west-1`

### Step 2: Add SSO Account in DinoDB

1. **Open Account Management**: Click the "+" button in the accounts panel
2. **Select SSO Authentication**: Choose "AWS SSO" as the authentication method
3. **Enter SSO Details**:
   - **Account Name**: A friendly name for this SSO configuration
   - **SSO Start URL**: Your organization's start URL
   - **SSO Region**: The region where your SSO is hosted
   - **Session Name**: Optional custom session name (defaults to "DinoDB-Session")

### Step 3: Complete Authentication Flow

1. **Initiate Authentication**: Click "Authenticate" to start the SSO flow
2. **Device Authorization**: DinoDB will display a verification code and URL
3. **Browser Authentication**: 
   - Your default browser will open to the verification page
   - Enter the displayed code when prompted
   - Complete your organization's authentication process
4. **Account Selection**: Once authenticated, select the AWS account and role to use

## Managing SSO Sessions

### Session Status

DinoDB displays the current status of your SSO sessions:

- **✅ Active**: Session is active with valid credentials
- **🔄 Refreshing**: Credentials are being automatically refreshed
- **⚠️ Expiring Soon**: Credentials will expire within 15 minutes
- **❌ Expired**: Session has expired and requires re-authentication

### Automatic Token Refresh

DinoDB automatically handles token refresh:

- **Background Refresh**: Tokens are refreshed automatically before expiration
- **Seamless Operation**: No interruption to your workflow
- **Secure Storage**: All tokens are stored securely in macOS Keychain

### Manual Session Management

- **Refresh Session**: Right-click an SSO account and select "Refresh Session"
- **Re-authenticate**: If tokens expire, click "Re-authenticate" to restart the flow
- **Clear Session**: Remove stored credentials with "Clear Session Data"

## Working with Multiple Accounts

### Account Discovery

DinoDB automatically discovers all AWS accounts available through your SSO:

- **Account List**: View all accessible accounts after authentication
- **Role Selection**: See available roles for each account
- **Quick Setup**: Add multiple accounts with different roles easily

### Account Switching

- **Favorites**: Mark frequently used accounts as favorites for quick access
- **Recent Accounts**: Recently used SSO accounts appear at the top
- **Role Indicators**: Clear visual indicators show which role is active

## Security Features

### Credential Protection

- **Keychain Storage**: All tokens and credentials stored in macOS Keychain
- **Memory Protection**: Sensitive data cleared from memory after use
- **No Disk Storage**: Credentials never written to unencrypted files

### Network Security

- **TLS Encryption**: All communication with AWS uses TLS 1.2+
- **Token Validation**: Continuous validation of token integrity
- **Secure Refresh**: Automatic token refresh without exposing credentials

### Audit and Compliance

- **Session Logging**: All SSO operations logged for audit purposes
- **Compliance Ready**: Meets enterprise security requirements
- **Access Tracking**: Integration with AWS CloudTrail for access monitoring

## Troubleshooting

### Common Issues

#### "SSO Client Not Registered" Error
- **Cause**: Initial client registration failed
- **Solution**: Clear session data and retry authentication
- **Prevention**: Ensure stable internet connection during setup

#### "Authentication Timeout" Error
- **Cause**: User didn't complete browser authentication within 10 minutes
- **Solution**: Restart the authentication flow
- **Prevention**: Complete browser authentication promptly

#### "Token Refresh Failed" Error
- **Cause**: Refresh token has expired
- **Solution**: Re-authenticate to obtain new tokens
- **Prevention**: Use DinoDB regularly to maintain active sessions

### Configuration Issues

#### Wrong SSO Region
- **Symptoms**: "Client not found" or authentication failures
- **Solution**: Verify the SSO region with your AWS administrator
- **Check**: Ensure the region matches your organization's SSO setup

#### Invalid Start URL
- **Symptoms**: Browser errors or invalid redirect
- **Solution**: Verify the start URL format and domain
- **Format**: Must be `https://your-org.awsapps.com/start`

### Network and Firewall Issues

If your organization has network restrictions:

- **Required Domains**: Ensure access to `*.awsapps.com` and `*.amazonaws.com`
- **Ports**: HTTPS (443) must be accessible
- **Proxy**: Configure proxy settings if required by your organization

## Advanced Configuration

### Session Customization

You can customize SSO session behavior:

```json
{
  "sessionName": "DinoDB-DevTeam",
  "tokenRefreshThreshold": 900,
  "automaticRefresh": true,
  "sessionTimeout": 43200
}
```

### Multiple SSO Configurations

DinoDB supports multiple SSO configurations for organizations with:

- **Multiple AWS Organizations**: Different SSO portals for different business units
- **Development/Production**: Separate SSO setups for different environments
- **Cross-Organization Access**: Guest access to partner AWS accounts

## Best Practices

### Security

1. **Regular Usage**: Use DinoDB regularly to maintain active sessions
2. **Session Monitoring**: Monitor session status in the accounts panel
3. **Prompt Re-authentication**: Don't ignore authentication prompts
4. **Secure Workstation**: Keep your Mac secure and up-to-date

### Operational

1. **Account Organization**: Use descriptive names for SSO accounts
2. **Role Selection**: Choose appropriate roles for your tasks
3. **Favorites Management**: Mark frequently used accounts as favorites
4. **Session Planning**: Plan extended work sessions to minimize re-authentication

### Team Coordination

1. **Shared Configuration**: Share SSO setup instructions with team members
2. **Role Standardization**: Coordinate role usage across your team
3. **Access Documentation**: Document which accounts are used for what purposes

## Support and Resources

### Getting Help

- **AWS Administrator**: Contact your AWS administrator for SSO configuration issues
- **DinoDB Support**: Use GitHub Issues for DinoDB-specific problems
- **Documentation**: Refer to AWS SSO documentation for advanced configuration

### Additional Resources

- [AWS SSO User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/)
- [IAM Identity Center Documentation](https://docs.aws.amazon.com/singlesignon/)
- [DinoDB GitHub Repository](https://github.com/Vegasq/dinodbapp)

---

*AWS SSO integration is a premium feature available exclusively in DinoDB PRO. [Upgrade to DinoDB PRO](https://dinodb.app/#pricing) to access enterprise authentication features.*