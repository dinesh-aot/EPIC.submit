# Integration and System Architecture

## Table of Contents
1. [Overview](#overview)
2. [System Components](#system-components)
3. [External System Integrations](#external-system-integrations)
4. [Authentication and Identity Management](#authentication-and-identity-management)
5. [Data Flow and Synchronization](#data-flow-and-synchronization)
6. [Email and Notification System](#email-and-notification-system)
7. [Document Storage and Management](#document-storage-and-management)
8. [Activity Logging and Audit Trail](#activity-logging-and-audit-trail)
9. [Security Architecture](#security-architecture)
10. [Business Continuity](#business-continuity)

---

## Overview

EPIC.submit operates as part of an integrated ecosystem of environmental assessment systems. It connects with multiple external systems to provide a seamless experience for users while maintaining data consistency and security across the platform.

### Ecosystem Context

EPIC.submit is one component in the broader EPIC (Environmental Assessment Process Information and Collaboration) suite of applications that support environmental assessment in British Columbia.

**EPIC Suite Components**:
- **EPIC.Track**: Project and work management system
- **EPIC.submit**: Submission management (this system)
- **EPIC.Document**: Document storage and retrieval
- **EPIC.Conditions**: Compliance condition repository
- **EPIC.Cron**: Background job scheduler and synchronization

### Integration Philosophy

**Principles**:
1. **Single Source of Truth**: Each system owns specific data domains
2. **Loose Coupling**: Systems can operate independently when needed
3. **Asynchronous Communication**: Non-blocking integration where possible
4. **Data Consistency**: Synchronization maintains consistency across systems
5. **Graceful Degradation**: System continues operating if integrations are temporarily unavailable

---

## System Components

### Frontend Application (EPIC.submit Web)

**Purpose**: User interface for proponents and EAO staff

**Characteristics**:
- Web-based application accessible via browser
- Responsive design works on desktop, tablet, and mobile
- Separate interfaces for proponents and staff
- Real-time updates and notifications
- Accessible design following WCAG guidelines

**User Experience**:
- Intuitive navigation
- Clear status indicators
- Guided workflows
- Contextual help
- Error prevention and recovery

**Technology Context** (minimal technical detail):
- Modern web framework
- Secure communication with backend
- Session management
- Client-side validation

### Backend API (EPIC.submit API)

**Purpose**: Business logic, data management, and integration orchestration

**Characteristics**:
- RESTful API architecture
- Handles all business rules and validations
- Manages database operations
- Coordinates with external systems
- Enforces security and access control

**Key Responsibilities**:
- User authentication and authorization
- Package and submission management
- Review workflow orchestration
- Document handling coordination
- Email notification triggering
- Activity logging
- Data validation and integrity

**API Structure**:
- Proponent-facing endpoints
- Staff-facing endpoints
- Operations/health check endpoints
- Clear separation of concerns

### Database

**Purpose**: Persistent storage of all submission data

**Characteristics**:
- Relational database structure
- Ensures data integrity through constraints
- Supports complex queries for reporting
- Regular backups for data protection
- Optimized for performance

**Data Stored**:
- User accounts and profiles
- Organizations and accounts
- Projects and assignments
- Packages and items
- Submissions and versions
- Review notes and decisions
- Activity logs
- System configuration

**Data Relationships**:
- Enforced referential integrity
- Cascading deletes where appropriate
- Audit trail preservation
- Version history maintenance

---

## External System Integrations

### EPIC.Track Integration

**Purpose**: Source of project information and metadata

**What EPIC.Track Provides**:
- Project details (name, type, location, status)
- Proponent organization information
- Certificate conditions and requirements
- Project timeline and milestones
- Environmental assessment history

**Integration Pattern**:
- **Pull Model**: EPIC.submit requests data from EPIC.Track
- **Scheduled Sync**: Periodic synchronization via EPIC.Cron
- **On-Demand Refresh**: Manual refresh when needed

**Data Synchronized**:
- Project metadata
- Proponent information
- Certificate conditions
- Project status updates

**Business Benefits**:
- Single source of truth for project data
- Automatic updates when projects change
- Consistent information across systems
- Reduced data entry duplication

**Synchronization Process**:
1. EPIC.Cron triggers scheduled sync (e.g., nightly)
2. EPIC.submit API calls EPIC.Track API
3. Project data retrieved
4. Local database updated with changes
5. Users see updated project information

**Handling Sync Issues**:
- If EPIC.Track unavailable, use cached data
- Log sync failures for investigation
- Retry failed syncs automatically
- Alert administrators if persistent failures

### EPIC.Document Integration

**Purpose**: Secure storage and retrieval of uploaded documents

**What EPIC.Document Provides**:
- Document upload capability
- Secure cloud storage
- Document retrieval
- Version management
- Virus scanning
- File format validation

**Integration Pattern**:
- **Direct Upload**: Files uploaded directly to document service
- **Reference Storage**: EPIC.submit stores document references
- **On-Demand Retrieval**: Documents fetched when users request them

**Document Lifecycle**:

**Upload Process**:
1. User selects file in EPIC.submit
2. File sent to EPIC.Document service
3. EPIC.Document scans for viruses
4. EPIC.Document stores in secure storage
5. EPIC.Document returns document ID
6. EPIC.submit stores document ID and metadata
7. User sees confirmation

**Retrieval Process**:
1. User requests to view/download document
2. EPIC.submit verifies user has access
3. EPIC.submit requests document from EPIC.Document
4. EPIC.Document validates request
5. EPIC.Document provides secure download link
6. User downloads document

**Security**:
- Documents encrypted in storage
- Access controlled by EPIC.submit
- Secure transmission (HTTPS)
- Virus scanning on upload
- Audit trail of access

**Business Benefits**:
- Scalable storage for large files
- Secure document handling
- Centralized document management
- Reduced storage costs
- Reliable backup and recovery

### EPIC.Conditions Integration

**Purpose**: Access to environmental certificate conditions for compliance validation

**What EPIC.Conditions Provides**:
- Certificate condition details
- Compliance requirements
- Condition categories and themes
- Related guidance documents

**Integration Pattern**:
- **Read-Only Access**: EPIC.submit queries but doesn't modify
- **On-Demand Lookup**: Conditions retrieved as needed
- **Reference Linking**: Submissions linked to specific conditions

**Use Cases**:

**During Package Creation**:
- Display relevant conditions for package type
- Help users understand requirements
- Link items to specific conditions

**During Review**:
- Staff reference conditions during evaluation
- Verify compliance with specific requirements
- Check condition interpretation

**For Reporting**:
- Track which conditions have been addressed
- Identify gaps in compliance
- Generate compliance reports

**Business Benefits**:
- Consistent condition information
- Clear compliance requirements
- Reduced ambiguity
- Better compliance tracking

### EPIC.Cron Integration

**Purpose**: Scheduled background tasks and system synchronization

**What EPIC.Cron Does**:
- Runs scheduled jobs
- Synchronizes data between systems
- Performs maintenance tasks
- Sends scheduled notifications
- Generates reports

**Scheduled Tasks**:

**Nightly Sync**:
- Synchronize project data from EPIC.Track
- Update proponent information
- Refresh certificate conditions
- Clean up temporary data

**Email Processing**:
- Process email queue
- Send pending notifications
- Retry failed emails
- Log email delivery status

**Data Maintenance**:
- Archive old data
- Clean up expired invitations
- Update calculated fields
- Optimize database

**Reporting**:
- Generate compliance reports
- Create usage statistics
- Produce audit reports
- Export data for analysis

**Business Benefits**:
- Automated routine tasks
- Consistent data across systems
- Reduced manual effort
- Timely notifications
- Regular maintenance

---

## Authentication and Identity Management

### Keycloak Identity Provider

**Purpose**: Centralized authentication and identity management

**What Keycloak Provides**:
- User authentication
- Single sign-on (SSO)
- Identity federation
- Role management
- Session management
- Multi-factor authentication support

**Integration with Government Identity Systems**:

**IDIR (Internal)**:
- BC government employee identity
- Used by EAO staff
- Managed by government IT
- Automatic provisioning
- Integrated with Active Directory

**BCeID (External)**:
- BC government external identity
- Used by proponents
- Self-service registration
- Business identity verification
- Supports multiple users per organization

### Authentication Flow

**User Login Process**:

1. **User Accesses EPIC.submit**
   - User navigates to application
   - System detects no active session
   - Redirects to login page

2. **Identity Provider Selection**
   - User selects IDIR (staff) or BCeID (proponent)
   - Redirected to Keycloak
   - Keycloak redirects to appropriate identity provider

3. **Authentication**
   - User enters credentials
   - Identity provider validates
   - Multi-factor authentication if required
   - Identity provider confirms identity

4. **Token Issuance**
   - Keycloak issues secure token (JWT)
   - Token contains user identity and roles
   - Token has expiration time
   - Token signed for security

5. **Return to EPIC.submit**
   - User redirected back to application
   - Token included in redirect
   - Application validates token
   - User session established

6. **Access Granted**
   - User sees appropriate interface
   - Permissions applied based on roles
   - Session maintained until logout or timeout

### Authorization

**How Permissions are Determined**:

1. **Token Validation**
   - Every request includes user token
   - System validates token signature
   - Checks token expiration
   - Extracts user identity and roles

2. **User Lookup**
   - System finds user in database
   - Retrieves user type (proponent/staff)
   - Gets assigned roles and permissions
   - Determines account and project access

3. **Permission Check**
   - System checks if user has required permission
   - Validates access to specific resources
   - Enforces data isolation (multi-tenancy)
   - Logs access attempts

4. **Access Decision**
   - Grant access if authorized
   - Deny access if not authorized
   - Log decision for audit
   - Return appropriate response

**Security Features**:
- Token-based authentication (stateless)
- Automatic token refresh
- Session timeout after inactivity
- Logout invalidates tokens
- Failed login tracking
- Account lockout after repeated failures

---

## Data Flow and Synchronization

### Project Data Synchronization

**Purpose**: Keep EPIC.submit project data consistent with EPIC.Track

**Synchronization Schedule**:
- **Nightly**: Full synchronization of all projects
- **On-Demand**: Manual refresh when needed
- **Real-Time**: Critical updates pushed immediately

**What Gets Synchronized**:

**Project Information**:
- Project name and description
- Project type and location
- Proponent organization
- Project status
- Certificate information
- Key dates and milestones

**Proponent Information**:
- Organization name
- Organization status
- Contact information
- Relationship to projects

**Synchronization Process**:

1. **Initiation**
   - EPIC.Cron triggers sync job
   - Or user requests manual refresh
   - Sync process begins

2. **Data Retrieval**
   - Query EPIC.Track for project data
   - Retrieve all relevant projects
   - Get associated proponent data
   - Fetch certificate information

3. **Comparison**
   - Compare retrieved data with local data
   - Identify new projects
   - Identify updated projects
   - Identify deleted/archived projects

4. **Update Local Database**
   - Add new projects
   - Update changed projects
   - Mark archived projects
   - Update proponent information

5. **Validation**
   - Verify data integrity
   - Check for conflicts
   - Resolve any issues
   - Log sync results

6. **Notification**
   - Notify users of significant changes
   - Alert administrators of issues
   - Log completion status

**Conflict Resolution**:
- EPIC.Track is authoritative source
- Local changes overwritten by sync
- Users notified of major changes
- Manual intervention for complex conflicts

**Business Impact**:
- Users always see current project information
- No manual data entry for projects
- Consistent data across systems
- Automatic updates reduce errors

### User Data Management

**User Creation Flow**:

1. **Invitation Created**
   - Admin creates invitation in EPIC.submit
   - Invitation stored in database
   - Email sent to invitee

2. **User Accepts Invitation**
   - User clicks invitation link
   - Authenticates via Keycloak
   - User identity retrieved from Keycloak

3. **User Account Created**
   - EPIC.submit creates user record
   - Links to Keycloak identity
   - Assigns specified role
   - Links to account and projects

4. **Ongoing Synchronization**
   - User profile updates from Keycloak
   - Role changes managed in EPIC.submit
   - Access permissions updated immediately

---

## Email and Notification System

### Email Queue System

**Purpose**: Reliable delivery of email notifications

**How It Works**:

**Email Creation**:
1. System event triggers email need
2. Email record created in queue
3. Email template selected
4. Recipient and data identified
5. Email marked as "Pending"

**Email Processing**:
1. EPIC.Cron processes email queue
2. Retrieves pending emails
3. Generates email content from template
4. Sends via email service
5. Updates email status

**Email Status Tracking**:
- **Pending**: Waiting to be sent
- **Sent**: Successfully delivered
- **Failed**: Delivery failed
- **Retry**: Will attempt again

**Retry Logic**:
- Failed emails automatically retried
- Multiple retry attempts
- Exponential backoff between retries
- Manual retry option for administrators

### Email Templates

**Template Types**:

**Invitation Emails**:
- New user invitation
- Organization invitation
- Project assignment notification

**Submission Emails**:
- Submission confirmation
- Package submitted notification (to staff)
- Status update notifications

**Review Emails**:
- Review assigned notification
- Review complete notification
- Decision notification (approval/rejection)

**Request Emails**:
- Revision request
- Update request
- Information request

**Template Components**:
- Subject line
- Greeting
- Body content with placeholders
- Call-to-action (links)
- Footer with contact information

**Personalization**:
- Recipient name
- Organization name
- Package/project details
- Specific actions required
- Relevant dates and deadlines

### Notification Preferences

**User Control**:
- Users can manage notification preferences
- Choose which notifications to receive
- Select notification frequency
- Opt out of non-critical notifications

**Default Notifications**:
- Critical notifications always sent
- Status changes
- Action required
- Decisions made

---

## Document Storage and Management

### Document Storage Architecture

**Storage Location**:
- Documents stored in EPIC.Document service
- Uses cloud-based object storage (S3-compatible)
- Scalable and reliable
- Geographically distributed for redundancy

**Storage Organization**:
- Documents organized by package
- Unique identifiers for each document
- Metadata stored separately in database
- Version history maintained

### Document Security

**Encryption**:
- Documents encrypted at rest
- Encrypted during transmission
- Encryption keys managed securely
- Regular key rotation

**Access Control**:
- Access controlled by EPIC.submit
- Users must authenticate
- Permissions verified before access
- All access logged

**Virus Scanning**:
- All uploads scanned for viruses
- Infected files rejected
- Users notified of issues
- Quarantine for suspicious files

### Document Lifecycle

**Upload**:
1. User selects file
2. Client-side validation (size, type)
3. Upload to EPIC.Document
4. Virus scan
5. Storage in secure location
6. Reference stored in database

**Storage**:
- Documents retained indefinitely
- All versions preserved
- Regular backups
- Disaster recovery procedures

**Retrieval**:
1. User requests document
2. Permission check
3. Generate secure download link
4. User downloads document
5. Access logged

**Deletion**:
- Documents never truly deleted
- Marked as inactive if needed
- Preserved for audit and compliance
- Accessible to administrators

---

## Activity Logging and Audit Trail

### What Gets Logged

**User Actions**:
- Login and logout
- Package creation and submission
- Document uploads and downloads
- Form submissions
- Status changes
- User invitations

**Staff Actions**:
- Review activities
- Status changes
- Approval decisions
- Note creation
- Update requests

**System Events**:
- Synchronization activities
- Email sending
- Errors and exceptions
- Performance metrics

### Log Information

**Each Log Entry Contains**:
- **Who**: User or system that performed action
- **What**: Description of action
- **When**: Timestamp (date and time)
- **Where**: What entity was affected (package, item, etc.)
- **Why**: Context or reason (if applicable)
- **Result**: Success or failure

### Log Visibility

**Public Logs** (visible to proponents):
- Their own actions
- EAO decisions affecting them
- Status changes
- Communication history

**Staff-Only Logs**:
- Internal review activities
- Staff discussions
- Draft decisions
- System administration

### Audit Trail Uses

**Compliance**:
- Demonstrate regulatory compliance
- Respond to audits
- Verify process adherence

**Troubleshooting**:
- Investigate issues
- Understand what happened
- Identify root causes

**Security**:
- Detect unauthorized access
- Track suspicious activity
- Support investigations

**Improvement**:
- Analyze usage patterns
- Identify bottlenecks
- Inform system enhancements

---

## Security Architecture

### Defense in Depth

**Multiple Security Layers**:

**Layer 1: Network Security**
- Firewall protection
- Intrusion detection
- DDoS protection
- Network segmentation

**Layer 2: Application Security**
- Secure coding practices
- Input validation
- Output encoding
- Error handling

**Layer 3: Authentication**
- Strong authentication (IDIR/BCeID)
- Multi-factor authentication support
- Session management
- Token-based security

**Layer 4: Authorization**
- Role-based access control
- Permission verification
- Data isolation
- Least privilege principle

**Layer 5: Data Security**
- Encryption at rest
- Encryption in transit
- Secure key management
- Data backup and recovery

### Security Monitoring

**Continuous Monitoring**:
- Failed login attempts
- Unauthorized access attempts
- Unusual activity patterns
- System errors and exceptions

**Alerting**:
- Security incidents trigger alerts
- Administrators notified
- Automated response for some threats
- Manual investigation for others

**Regular Reviews**:
- Security audits
- Vulnerability assessments
- Penetration testing
- Code reviews

### Data Privacy

**Personal Information Protection**:
- Minimal data collection
- Purpose-specific use
- Secure storage
- Limited retention
- User access to own data

**Compliance**:
- Freedom of Information and Protection of Privacy Act (FOIPPA)
- Privacy Impact Assessment completed
- Regular privacy reviews
- Staff training on privacy

---

## Business Continuity

### High Availability

**System Redundancy**:
- Multiple application servers
- Database replication
- Load balancing
- Automatic failover

**Uptime Target**: 99.5% availability (approximately 3.5 hours downtime per month)

**Maintenance Windows**:
- Scheduled maintenance during low-usage periods
- Users notified in advance
- Minimal disruption
- Quick recovery

### Backup and Recovery

**Backup Strategy**:

**Database Backups**:
- Full backup daily
- Incremental backups hourly
- Transaction log backups continuously
- Retained for 30 days

**Document Backups**:
- Continuous replication
- Geographic distribution
- Version history preserved
- Long-term retention

**Recovery Objectives**:
- **Recovery Time Objective (RTO)**: 4 hours
- **Recovery Point Objective (RPO)**: 1 hour
- Minimal data loss
- Quick restoration

**Disaster Recovery**:
- Documented recovery procedures
- Regular testing of recovery
- Off-site backups
- Alternative hosting capability

### Incident Response

**Incident Types**:
- Security breaches
- System outages
- Data corruption
- Performance degradation

**Response Process**:
1. **Detection**: Incident identified
2. **Assessment**: Severity evaluated
3. **Containment**: Prevent further impact
4. **Resolution**: Fix the issue
5. **Recovery**: Restore normal operation
6. **Review**: Learn and improve

**Communication**:
- Users notified of incidents
- Status updates provided
- Resolution timeline communicated
- Post-incident report shared

---

## Performance and Scalability

### Performance Optimization

**Response Time Targets**:
- Page load: < 2 seconds
- API response: < 500 milliseconds
- Document upload: Depends on file size
- Search results: < 1 second

**Optimization Techniques**:
- Database query optimization
- Caching frequently accessed data
- Efficient code algorithms
- Content delivery network (CDN)
- Asynchronous processing

### Scalability

**Handling Growth**:
- System designed to scale horizontally
- Add more servers as needed
- Database can be scaled
- Storage is virtually unlimited

**Current Capacity**:
- Supports hundreds of concurrent users
- Thousands of packages
- Millions of documents
- Can scale to meet demand

**Monitoring**:
- Performance metrics tracked
- Capacity planning
- Proactive scaling
- Resource optimization

---

## Integration Best Practices

### Error Handling

**Graceful Degradation**:
- If external system unavailable, use cached data
- Inform users of limitations
- Queue operations for later
- Retry automatically

**User Communication**:
- Clear error messages
- Explain what happened
- Suggest next steps
- Provide support contact

### Data Consistency

**Ensuring Consistency**:
- Regular synchronization
- Validation checks
- Conflict resolution
- Manual reconciliation when needed

**Handling Discrepancies**:
- Log inconsistencies
- Alert administrators
- Investigate root cause
- Implement fixes

### Monitoring and Alerting

**What's Monitored**:
- System availability
- Integration health
- Performance metrics
- Error rates
- User activity

**Alerting**:
- Critical issues trigger immediate alerts
- Warnings for potential issues
- Regular status reports
- Dashboard for real-time monitoring

---

## Future Integration Opportunities

### Potential Enhancements

**GIS Integration**:
- Map-based project visualization
- Spatial data submission
- Geographic analysis
- Location-based reporting

**Analytics Platform**:
- Advanced reporting
- Trend analysis
- Predictive analytics
- Business intelligence

**Public Portal**:
- Public access to approved submissions
- Transparency and accountability
- Searchable database
- Download capabilities

**Mobile Application**:
- Field data collection
- Photo uploads from site
- Offline capability
- Real-time updates

**Automated Compliance Checking**:
- AI-assisted review
- Automatic validation
- Anomaly detection
- Risk scoring

---

*This document covers integration and system architecture in EPIC.submit. Together with the other business documentation, it provides a complete understanding of how the system operates and delivers value to users.*
