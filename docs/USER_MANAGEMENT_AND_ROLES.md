# User Management and Roles

## Table of Contents
1. [Overview](#overview)
2. [User Types](#user-types)
3. [User Onboarding Process](#user-onboarding-process)
4. [Proponent Roles and Permissions](#proponent-roles-and-permissions)
5. [Staff Roles and Permissions](#staff-roles-and-permissions)
6. [Account Structure](#account-structure)
7. [User Lifecycle Management](#user-lifecycle-management)
8. [Security and Access Control](#security-and-access-control)

---

## Overview

EPIC.submit uses a role-based access control (RBAC) system to ensure users have appropriate access to features and data based on their responsibilities. The system supports two distinct user types with different role structures and permissions.

### Key Principles

1. **Least Privilege**: Users are granted only the permissions necessary for their role
2. **Separation of Duties**: Different roles handle different aspects of the submission process
3. **Multi-Tenancy**: Proponent users can only access their organization's data
4. **Audit Trail**: All user actions are logged for accountability
5. **Flexible Assignment**: Users can be assigned to specific projects or packages

---

## User Types

### 1. Proponent Users

**Definition**: Users who work for organizations that hold environmental certificates or exemptions.

**Characteristics:**
- Belong to a specific proponent organization
- Have access to their organization's account
- Can be assigned to one or more projects
- Authenticate using BCeID (BC government external identity)
- Create and submit packages
- Respond to EAO requests

**Example Users:**
- Environmental managers at mining companies
- Compliance officers at energy facilities
- Consultants working on behalf of certificate holders
- Project managers responsible for submissions

### 2. Staff Users

**Definition**: Employees of the Environmental Assessment Office who review and approve submissions.

**Characteristics:**
- Work for the EAO
- Have access to all proponent submissions
- Authenticate using IDIR (BC government internal identity)
- Review and approve packages
- Request revisions and additional information
- Create internal review documents

**Example Users:**
- Environmental assessment officers
- Subject matter experts (biologists, engineers, etc.)
- EAO managers who provide final approvals
- Administrative staff who manage user access

---

## User Onboarding Process

### Proponent User Onboarding

**Step 1: Invitation Creation**

**Who Initiates:**
- EAO staff (for new organizations)
- Account administrators (for new team members)
- Project administrators (for project-specific users)

**Information Required:**
- User's email address
- User's full name
- Role to be assigned
- Projects or packages to grant access to
- Proponent organization

**Business Rules:**
- Email must be unique within the account
- Cannot invite a user who already has access
- Invitation expires after 7 days
- Only one pending invitation per email address

**Step 2: Invitation Delivery**

**What Happens:**
- System generates unique invitation token
- Email sent to invitee with secure link
- Email includes:
  - Organization name
  - Role being assigned
  - Link to accept invitation
  - Expiration date
  - Instructions for first-time login

**Step 3: Invitation Acceptance**

**User Actions:**
1. Click invitation link in email
2. Authenticate using BCeID
3. Review and accept terms of service
4. Complete profile information
5. Gain access to assigned projects/packages

**System Actions:**
- Validate invitation token
- Check expiration date
- Create user account
- Assign specified role
- Link user to account and projects
- Mark invitation as "Used"
- Send confirmation email

**Step 4: First Login**

**What User Sees:**
- Welcome message
- Dashboard with assigned projects
- List of packages they can access
- Quick start guide

### Staff User Onboarding

**Process:**
- Managed by EAO system administrators
- Users authenticate with existing IDIR credentials
- Assigned to appropriate Keycloak groups
- Roles determined by group membership
- Immediate access upon group assignment

---

## Proponent Roles and Permissions

### Role Hierarchy

```
Account Primary Admin (Highest Authority)
    ↓
Project Admin
    ↓
Submission Admin
    ↓
Specific Submission Contributor (Most Limited)
```

### 1. Account Primary Admin

**Purpose**: Manage the entire organization's account and all associated projects.

**Who Should Have This Role:**
- Senior environmental manager
- Compliance director
- One or two key personnel per organization

**Permissions:**

**User Management:**
- ✅ Invite new users to the account
- ✅ Assign roles to users
- ✅ Remove users from the account
- ✅ View all users in the account
- ✅ Modify user roles and permissions

**Project Access:**
- ✅ Access all projects in the account
- ✅ Create packages for any project
- ✅ View all packages across all projects
- ✅ Submit packages for any project

**Package Management:**
- ✅ Create new packages
- ✅ Edit any package in the account
- ✅ Delete draft packages
- ✅ Submit packages to EAO
- ✅ Respond to EAO requests
- ✅ Create resubmissions

**Data Access:**
- ✅ View all submissions
- ✅ Access all documents
- ✅ View activity logs
- ✅ Export data

**Restrictions:**
- ❌ Cannot access other organizations' data
- ❌ Cannot modify submitted packages (can only create new versions)
- ❌ Cannot delete submitted packages

**Business Scenarios:**

*Scenario 1: New Team Member*
- Account admin receives request to add new environmental coordinator
- Admin sends invitation with "Submission Admin" role
- New user gains access to all active projects

*Scenario 2: Project Completion*
- Project reaches completion
- Admin removes users who no longer need access
- Admin archives completed packages

*Scenario 3: Role Change*
- User promoted to senior role
- Admin upgrades user from Contributor to Project Admin
- User gains expanded permissions

### 2. Project Admin

**Purpose**: Manage submissions for specific projects.

**Who Should Have This Role:**
- Project managers
- Site environmental coordinators
- Consultants assigned to specific projects

**Permissions:**

**User Management:**
- ✅ Invite users to assigned projects
- ✅ Assign roles within their projects
- ✅ View users assigned to their projects
- ❌ Cannot manage account-wide users

**Project Access:**
- ✅ Access assigned projects only
- ✅ View all packages in assigned projects
- ✅ Create packages for assigned projects

**Package Management:**
- ✅ Create new packages for their projects
- ✅ Edit packages in their projects
- ✅ Submit packages to EAO
- ✅ Respond to EAO requests
- ✅ Create resubmissions

**Data Access:**
- ✅ View submissions in their projects
- ✅ Access documents in their projects
- ✅ View activity logs for their projects

**Restrictions:**
- ❌ Cannot access projects they're not assigned to
- ❌ Cannot manage account-level settings
- ❌ Cannot remove users from the account

**Business Scenarios:**

*Scenario 1: Multi-Project Organization*
- Mining company has three mine sites
- Each site has a Project Admin
- Each admin manages only their site's submissions

*Scenario 2: Consultant Assignment*
- External consultant hired for specific project
- Assigned as Project Admin for that project only
- Cannot see other projects in the account

### 3. Submission Admin

**Purpose**: Create and manage submission packages without user management responsibilities.

**Who Should Have This Role:**
- Environmental technicians
- Compliance coordinators
- Document preparers

**Permissions:**

**Package Management:**
- ✅ Create new packages
- ✅ Edit packages they have access to
- ✅ Submit packages to EAO
- ✅ Upload documents
- ✅ Fill out forms
- ✅ Respond to EAO requests
- ✅ Create resubmissions

**Data Access:**
- ✅ View packages they're assigned to
- ✅ Access documents in their packages
- ✅ View activity logs for their work

**Restrictions:**
- ❌ Cannot invite users
- ❌ Cannot assign roles
- ❌ Cannot access packages they're not assigned to
- ❌ Cannot manage projects

**Business Scenarios:**

*Scenario 1: Document Preparation*
- Technician prepares annual management plan
- Has access to create and edit the package
- Submits to Project Admin for review before EAO submission

*Scenario 2: Specialized Contributor*
- Biologist responsible for wildlife monitoring section
- Given access to specific package
- Completes their section, others handle remaining items

### 4. Specific Submission Contributor

**Purpose**: Contribute to specific packages only, with limited access.

**Who Should Have This Role:**
- Subject matter experts contributing to one section
- External consultants for specific deliverables
- Temporary staff for particular submissions

**Permissions:**

**Package Management:**
- ✅ Edit assigned packages only
- ✅ Upload documents to assigned items
- ✅ Fill out forms in assigned items
- ✅ View package status

**Data Access:**
- ✅ View only packages they're assigned to
- ✅ Access documents in assigned packages
- ❌ Cannot view other packages

**Restrictions:**
- ❌ Cannot create new packages
- ❌ Cannot submit packages to EAO
- ❌ Cannot invite users
- ❌ Cannot access unassigned packages
- ❌ Cannot delete content

**Business Scenarios:**

*Scenario 1: External Expert*
- Archaeologist hired to complete heritage section
- Given contributor access to specific package
- Completes their section, no access to other content

*Scenario 2: Temporary Staff*
- Summer student helps with data entry
- Limited access to specific packages
- Cannot submit or make major changes

### Permission Matrix

| Permission | Account Primary Admin | Project Admin | Submission Admin | Contributor |
|------------|----------------------|---------------|------------------|-------------|
| Invite users to account | ✅ | ❌ | ❌ | ❌ |
| Invite users to project | ✅ | ✅ | ❌ | ❌ |
| Manage user roles | ✅ | ✅ (project only) | ❌ | ❌ |
| Access all projects | ✅ | ❌ | ❌ | ❌ |
| Create packages | ✅ | ✅ | ✅ | ❌ |
| Edit packages | ✅ | ✅ | ✅ | ✅ (assigned only) |
| Submit packages | ✅ | ✅ | ✅ | ❌ |
| Delete draft packages | ✅ | ✅ | ✅ | ❌ |
| View all account data | ✅ | ❌ | ❌ | ❌ |
| Respond to EAO requests | ✅ | ✅ | ✅ | ❌ |
| Create resubmissions | ✅ | ✅ | ✅ | ❌ |

---

## Staff Roles and Permissions

### Staff Role Structure

Staff roles are managed through Keycloak groups and provide different levels of access to system features.

### 1. EAO Edit (eao_edit)

**Purpose**: Review and manage submissions with full editing capabilities.

**Who Has This Role:**
- Environmental assessment officers
- Project leads
- Senior reviewers

**Permissions:**
- ✅ View all proponent submissions
- ✅ Conduct reviews
- ✅ Add review notes
- ✅ Request revisions
- ✅ Approve submissions
- ✅ Reject submissions
- ✅ Create internal documents
- ✅ Update package status
- ✅ Assign reviewers
- ✅ View activity logs

**Business Scenarios:**

*Scenario 1: Management Plan Review*
- Officer receives new management plan submission
- Reviews all items for completeness
- Adds review notes for each section
- Requests revision for inadequate monitoring plan
- Approves after satisfactory resubmission

*Scenario 2: Consultation Check*
- Officer conducts consultation record review
- Verifies Indigenous consultation requirements met
- Updates status to "Passed Consultation Check"
- Assigns to technical reviewer for next stage

### 2. EAO View (eao_view)

**Purpose**: Read-only access to submissions for monitoring and oversight.

**Who Has This Role:**
- Managers
- Auditors
- Administrative staff
- Observers

**Permissions:**
- ✅ View all submissions
- ✅ Access all documents
- ✅ View review notes
- ✅ View activity logs
- ✅ Generate reports
- ❌ Cannot edit submissions
- ❌ Cannot change status
- ❌ Cannot add review notes

**Business Scenarios:**

*Scenario 1: Management Oversight*
- Manager reviews team's work
- Monitors review progress
- Identifies bottlenecks
- Does not directly modify submissions

*Scenario 2: Audit Review*
- Auditor examines submission history
- Reviews decision rationale
- Verifies process compliance
- Read-only access ensures audit integrity

### 3. EAO Create (eao_create)

**Purpose**: Create internal documents and analysis reports.

**Who Has This Role:**
- Technical specialists
- Analysts
- Support staff

**Permissions:**
- ✅ View submissions
- ✅ Create internal documents
- ✅ Upload analysis files
- ✅ Add technical notes
- ❌ Cannot approve/reject submissions
- ❌ Cannot change package status

**Business Scenarios:**

*Scenario 1: Technical Analysis*
- Biologist creates species impact analysis
- Uploads report as internal document
- Attached to package for reviewer reference
- Not visible to proponent

### 4. Extended EAO Edit (extended_eao_edit)

**Purpose**: Advanced editing capabilities for senior staff.

**Who Has This Role:**
- Senior managers
- Program directors
- Executive staff

**Permissions:**
- ✅ All EAO Edit permissions
- ✅ Override decisions
- ✅ Modify historical records (with justification)
- ✅ Access archived data
- ✅ Bulk operations

### 5. Manage Users (manage-users)

**Purpose**: Administer user accounts and access.

**Who Has This Role:**
- System administrators
- IT support staff
- Security officers

**Permissions:**
- ✅ Invite proponent organizations
- ✅ Create staff accounts
- ✅ Assign roles
- ✅ Deactivate users
- ✅ Reset passwords
- ✅ View user activity
- ✅ Manage permissions

---

## Account Structure

### What is an Account?

An account is the organizational container that holds:
- Proponent organization information
- Users associated with the organization
- Projects assigned to the organization
- All submission packages
- Activity history

### Account Characteristics

**One-to-One Relationship:**
- One account per proponent organization
- One proponent organization per account
- Cannot merge or split accounts

**Multi-Project Support:**
- Account can have multiple projects
- Projects linked through Account Projects
- Users can access multiple projects within their account

**User Isolation:**
- Users can only access their own account's data
- No cross-account visibility for proponents
- Staff can see all accounts

### Account Lifecycle

**1. Account Creation**

**Trigger:** New proponent organization needs to submit documents

**Process:**
1. EAO staff identifies need for new account
2. Staff creates invitation for organization
3. Invitation includes:
   - Organization name
   - Initial project assignments
   - Primary admin designation
4. Organization representative accepts invitation
5. Account activated

**2. Account Operation**

**Ongoing Activities:**
- Users added and removed
- Projects added as new certificates issued
- Packages created and submitted
- Data accumulated over time

**3. Account Maintenance**

**Regular Tasks:**
- User access reviews
- Role updates
- Project assignments
- Terms of service acceptance

**4. Account Deactivation**

**Triggers:**
- Certificate surrendered
- Project completed
- Organization dissolved

**Process:**
- Mark account as inactive
- Preserve data for records
- Prevent new logins
- Maintain read-only access for EAO

---

## User Lifecycle Management

### Active User Management

**Adding Users:**
1. Authorized user creates invitation
2. Invitation sent via email
3. Recipient accepts and authenticates
4. User account created
5. Access granted

**Modifying User Access:**
1. Administrator identifies need for change
2. Updates user role or project assignments
3. Changes take effect immediately
4. User notified of changes
5. Activity logged

**Removing Users:**
1. Administrator deactivates user
2. User loses access immediately
3. Historical data preserved
4. Activity logs retained
5. User can be reactivated if needed

### User Status

**Active:**
- Can log in
- Has full role permissions
- Receives notifications
- Can perform assigned tasks

**Inactive:**
- Cannot log in
- No system access
- Historical data preserved
- Can be reactivated

**Pending:**
- Invitation sent but not accepted
- No system access yet
- Invitation can be resent or revoked

### Terms of Service

**Requirement:**
- All users must accept terms of service
- Required on first login
- Updated terms require re-acceptance
- Cannot use system without acceptance

**Content:**
- Acceptable use policies
- Data privacy notices
- Compliance requirements
- User responsibilities

---

## Security and Access Control

### Authentication

**Proponent Users:**
- Authenticate via BCeID
- Government-issued identity
- Multi-factor authentication supported
- Session timeout after inactivity

**Staff Users:**
- Authenticate via IDIR
- BC government employee identity
- Integrated with government systems
- Single sign-on enabled

### Authorization

**Token-Based:**
- JWT (JSON Web Token) issued on login
- Token contains user identity and roles
- Token validated on every request
- Token expires after set period

**Role Verification:**
- Every action checks user permissions
- Role requirements enforced at API level
- Unauthorized actions blocked
- Attempts logged for security monitoring

### Data Isolation

**Multi-Tenancy:**
- Proponent users see only their account data
- Database queries filtered by account
- No cross-account data leakage
- Staff can access all accounts

**Project-Level Isolation:**
- Users see only assigned projects
- Package access controlled by assignment
- Document access restricted to authorized users

### Audit and Compliance

**Activity Logging:**
- All user actions logged
- Login/logout tracked
- Failed access attempts recorded
- Logs immutable and timestamped

**Access Reviews:**
- Periodic review of user access
- Identification of inactive users
- Role appropriateness assessment
- Removal of unnecessary permissions

### Security Best Practices

**For Administrators:**
- Grant minimum necessary permissions
- Review user access regularly
- Deactivate users promptly when no longer needed
- Monitor for suspicious activity
- Use strong authentication methods

**For Users:**
- Protect login credentials
- Log out when finished
- Report suspicious activity
- Don't share accounts
- Accept only legitimate invitations

---

## Business Scenarios

### Scenario 1: New Organization Onboarding

**Situation:** Mining company receives environmental certificate and needs to submit first management plan.

**Process:**
1. EAO staff creates invitation for company
2. Company's environmental manager receives invitation
3. Manager accepts, becomes Account Primary Admin
4. Manager invites project team members
5. Team members assigned appropriate roles
6. Team begins working on management plan

**Outcome:** Organization fully onboarded with appropriate access structure.

### Scenario 2: Consultant Engagement

**Situation:** Proponent hires external consultant to prepare IEM report.

**Process:**
1. Project Admin invites consultant
2. Consultant assigned as Specific Submission Contributor
3. Consultant given access to IEM package only
4. Consultant completes assigned sections
5. Project Admin reviews and submits
6. Consultant access removed after project completion

**Outcome:** Consultant has appropriate limited access for their role.

### Scenario 3: Staff Turnover

**Situation:** Environmental coordinator leaves company, replacement hired.

**Process:**
1. Account Admin deactivates departing user
2. Admin invites new coordinator
3. New user assigned same role as predecessor
4. New user gains access to ongoing packages
5. Historical data preserved showing both users' contributions

**Outcome:** Seamless transition with maintained audit trail.

### Scenario 4: Role Escalation

**Situation:** Submission Admin promoted to project management role.

**Process:**
1. Account Admin updates user role to Project Admin
2. User gains expanded permissions
3. User can now invite team members
4. User maintains access to existing packages
5. Change logged in activity history

**Outcome:** User permissions match new responsibilities.

---

*This document covers user management and roles in EPIC.submit. For information on submission workflows, see the Package and Submission Workflow documentation.*
