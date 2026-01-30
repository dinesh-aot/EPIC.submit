# EPIC.submit - Business Overview

## Table of Contents
1. [Introduction](#introduction)
2. [System Purpose](#system-purpose)
3. [Key Stakeholders](#key-stakeholders)
4. [Core Business Capabilities](#core-business-capabilities)
5. [System Architecture Overview](#system-architecture-overview)
6. [Business Value](#business-value)

---

## Introduction

**EPIC.submit** is an online submission management system developed for the Environmental Assessment Office (EAO) of British Columbia. The system enables Certificate and Exemption Holders (proponents) to submit management plans, monitoring reports, and other post-certificate documents to the EAO in a structured, trackable, and efficient manner.

The system replaces manual submission processes with a digital workflow that ensures compliance, maintains audit trails, and facilitates communication between proponents and EAO staff.

---

## System Purpose

### Primary Objectives

1. **Streamline Document Submission**: Provide a centralized platform for proponents to submit required documents to the EAO
2. **Ensure Compliance**: Track and verify that submissions meet environmental certificate conditions
3. **Enable Collaboration**: Allow multiple users within an organization to work together on submissions
4. **Maintain Audit Trails**: Record all activities and changes for accountability and compliance
5. **Facilitate Review**: Provide EAO staff with tools to review, approve, or request revisions to submissions

### Business Problem Solved

Before EPIC.submit, proponents submitted documents through email or physical mail, leading to:
- Lost or misplaced submissions
- Difficulty tracking submission status
- No version control for documents
- Manual coordination between multiple stakeholders
- Limited visibility into the review process

EPIC.submit addresses these challenges by providing a structured, transparent, and auditable submission process.

---

## Key Stakeholders

### 1. Certificate/Exemption Holders (Proponents)

**Who They Are:**
- Organizations that hold environmental assessment certificates or exemptions
- Typically mining companies, energy projects, infrastructure developers, or industrial facilities
- Required to submit regular reports and plans to maintain compliance

**What They Do in the System:**
- Create and submit management plans
- Upload monitoring reports
- Provide consultation records
- Respond to EAO feedback and requests
- Manage team members who work on submissions

**Example Organizations:**
- Mining companies with approved mine projects
- LNG facilities with environmental certificates
- Major infrastructure projects (highways, pipelines)

### 2. EAO Staff

**Who They Are:**
- Environmental Assessment Office employees
- Subject matter experts in various environmental disciplines
- Managers who provide final approvals

**What They Do in the System:**
- Review submitted documents and forms
- Conduct consultation checks
- Request additional information or revisions
- Approve or reject submissions
- Create internal review notes and documents
- Monitor compliance with certificate conditions

**Staff Roles:**
- **Reviewers**: Conduct technical reviews of submissions
- **Managers**: Provide final approval decisions
- **Administrators**: Manage user access and system configuration

### 3. System Administrators

**Who They Are:**
- Technical staff responsible for system operation
- User access managers

**What They Do:**
- Invite new proponent organizations
- Manage user accounts and permissions
- Monitor system health and performance
- Troubleshoot issues

---

## Core Business Capabilities

### 1. Account and Organization Management

**Business Need**: Multiple organizations need secure, isolated workspaces to manage their submissions.

**How It Works:**
- Each proponent organization has one account
- Accounts are linked to projects from the EPIC.Track system
- Users within an account can access projects assigned to their organization
- Account administrators can invite and manage team members

**Business Rules:**
- One account per proponent organization
- Accounts can have multiple projects
- Users can only access their organization's data
- Account creation requires EAO approval

### 2. User Management and Access Control

**Business Need**: Different users need different levels of access based on their responsibilities.

**How It Works:**
- Users are invited via email with time-limited invitation links
- Users authenticate through government identity systems (IDIR for staff, BCeID for proponents)
- Role-based permissions control what users can do
- Users can be assigned to specific projects or packages

**User Types:**
- **Proponent Users**: Work for certificate holders
- **Staff Users**: Work for the EAO

**Access Levels:**
- Account-wide access (administrators)
- Project-specific access (project managers)
- Package-specific access (contributors)

### 3. Project Management

**Business Need**: Link submissions to specific environmental assessment projects.

**How It Works:**
- Projects are synchronized from the EPIC.Track system
- Each project represents an environmental assessment with approved conditions
- Proponents can only submit documents for projects they're associated with
- Projects contain metadata like project name, type, location, and status

**Project Information Includes:**
- Project name and description
- Proponent organization
- Project type (mine, energy, infrastructure, etc.)
- Environmental conditions and requirements
- Project status and timeline

### 4. Package Creation and Management

**Business Need**: Organize related documents and forms into structured submission packages.

**What is a Package?**
A package is a container for a complete submission. It organizes all required documents, forms, and information for a specific submission type.

**Package Types:**

1. **Management Plans**
   - Annual compliance plans required by certificate conditions
   - Include project overview, management strategies, monitoring plans
   - Typically submitted annually

2. **Independent Environmental Monitor (IEM) Reports**
   - Reports from third-party environmental monitors
   - Verify compliance with certificate conditions
   - Submitted quarterly or as required

3. **Consultation Records**
   - Documentation of Indigenous consultation activities
   - Required to demonstrate meaningful engagement
   - Submitted as consultation milestones are reached

**Package Components:**
- **Items**: Individual sections within a package (e.g., "Project Overview", "Contact Information", "Monitoring Plan")
- **Metadata**: Package-specific information like contacts, dates, and references
- **Documents**: Uploaded files (PDFs, spreadsheets, images)
- **Forms**: Structured data entry fields

**Package Lifecycle:**
1. **Creation**: User creates a new package for a project
2. **Drafting**: User fills in items with documents and forms
3. **Submission**: User submits completed package to EAO
4. **Review**: EAO staff review the submission
5. **Decision**: Package is approved, rejected, or revision is requested
6. **Resubmission** (if needed): User creates new version with updates

### 5. Submission Workflow

**Business Need**: Manage the complete lifecycle of document submissions from creation to approval.

**Submission Process:**

**Step 1: Package Creation**
- User selects a project and package type
- System automatically creates required items based on package type
- User sees a checklist of items to complete

**Step 2: Content Entry**
- User uploads documents or fills out forms for each item
- System validates file types and sizes
- Users can save drafts and return later
- Version control tracks all changes

**Step 3: Internal Review**
- Users review their submission before sending to EAO
- Team members can collaborate and provide feedback
- Account administrators can review before submission

**Step 4: Submission to EAO**
- User clicks "Submit" to send package to EAO
- System validates that all required items are complete
- Confirmation email sent to submitter
- Package status changes to "Submitted"
- EAO staff are notified of new submission

**Step 5: EAO Review**
- Staff conduct consultation checks
- Technical reviewers assess content
- Managers provide final approval
- Staff can add internal notes and documents

**Step 6: Decision**
- **Approved**: Submission meets requirements
- **Rejected**: Submission does not meet requirements
- **Revision Required**: Proponent must make changes and resubmit

**Step 7: Resubmission (if needed)**
- System creates new package version
- Previous submission content is copied
- User makes required changes
- Resubmission follows same review process

### 6. Review and Approval Process

**Business Need**: Structured review process ensures thorough evaluation of submissions.

**Review Stages:**

**Stage 1: Consultation Check**
- Verify Indigenous consultation requirements are met
- Check consultation records and documentation
- Outcome: Pass or Fail

**Stage 2: Technical Review**
- Subject matter experts review content
- Assess compliance with certificate conditions
- Evaluate technical adequacy
- Identify gaps or concerns

**Stage 3: Manager Approval**
- Senior staff review recommendations
- Make final approval decision
- Can request additional information or revisions

**Review Tools:**
- **Item-level reviews**: Review each section independently
- **Review notes**: Staff can add comments visible to proponents
- **Internal documents**: Staff can attach internal analysis documents
- **Status tracking**: Clear visibility into review progress

### 7. Communication and Notifications

**Business Need**: Keep all stakeholders informed of submission status and required actions.

**Notification Types:**

1. **Invitation Emails**
   - Sent when new users are invited
   - Include secure link to accept invitation
   - Expire after 7 days

2. **Submission Confirmations**
   - Sent when package is submitted
   - Confirm receipt by EAO
   - Include submission reference number

3. **Status Updates**
   - Notify proponents of review progress
   - Alert when decisions are made
   - Inform of revision requests

4. **Resubmission Requests**
   - Sent when revisions are required
   - Include details of what needs to be changed
   - Provide link to create new version

5. **Update Requests**
   - Staff can request additional information
   - Proponent receives notification with details
   - Can respond without full resubmission

### 8. Activity Logging and Audit Trail

**Business Need**: Maintain complete record of all activities for accountability and compliance.

**What is Logged:**
- All user actions (submissions, updates, deletions)
- All staff actions (reviews, approvals, rejections)
- Status changes and transitions
- Document uploads and replacements
- User invitations and access changes

**Log Information Includes:**
- Who performed the action
- What action was performed
- When it occurred
- What entity was affected (package, item, submission)
- Version information

**Visibility Control:**
- Some logs are visible to proponents (their own actions, EAO decisions)
- Some logs are staff-only (internal review notes, discussions)

### 9. Version Control

**Business Need**: Track changes over time and maintain history of submissions.

**Package Versioning:**
- Each resubmission creates a new package version
- Version numbers increment (v1, v2, v3, etc.)
- Previous versions remain accessible for reference
- Version history shows what changed and why

**Submission Versioning:**
- Individual documents can be replaced
- Major and minor version numbers (e.g., 1.1, 1.2, 2.0)
- Version history tracks all changes
- Users can view previous versions

**Benefits:**
- Complete audit trail
- Ability to compare versions
- Rollback capability if needed
- Historical reference for compliance

---

## System Architecture Overview

### High-Level Components

**1. EPIC.submit Web Application (Frontend)**
- User interface for proponents and staff
- Built with React and TypeScript
- Responsive design for desktop and mobile
- Accessible and user-friendly

**2. EPIC.submit API (Backend)**
- Business logic and data management
- Built with Python Flask
- RESTful API architecture
- Handles authentication and authorization

**3. Database**
- PostgreSQL relational database
- Stores all submission data
- Maintains relationships between entities
- Ensures data integrity

**4. Authentication Service (Keycloak)**
- Manages user authentication
- Integrates with IDIR (government staff)
- Integrates with BCeID (external users)
- Issues secure access tokens

### External System Integrations

**1. EPIC.Track**
- Source of project information
- Provides project metadata
- Synchronized periodically
- Ensures consistent project data

**2. EPIC.Document**
- Document storage service
- Handles file uploads and downloads
- Uses secure cloud storage (S3)
- Manages large files efficiently

**3. EPIC.Conditions**
- Repository of environmental conditions
- Used for compliance validation
- Provides condition details
- Links submissions to specific conditions

**4. Email Service**
- Sends automated notifications
- Delivers invitation emails
- Provides status updates
- Ensures timely communication

### Data Flow

1. **User Authentication**: User logs in via Keycloak (IDIR/BCeID)
2. **Project Selection**: User selects project from EPIC.Track data
3. **Package Creation**: User creates package in EPIC.submit
4. **Document Upload**: Files stored in EPIC.Document
5. **Submission**: Package submitted for review
6. **Review Process**: Staff review using EPIC.submit tools
7. **Notification**: Email sent to proponent with decision
8. **Audit Logging**: All actions recorded in database

---

## Business Value

### For Proponents

**Efficiency Gains:**
- Reduced time to prepare and submit documents
- Clear guidance on requirements
- Ability to save drafts and work incrementally
- Team collaboration on submissions

**Transparency:**
- Real-time visibility into submission status
- Clear communication of review progress
- Understanding of what's required for approval

**Compliance:**
- Structured process ensures nothing is missed
- Automatic validation of requirements
- Historical record of all submissions

**Cost Savings:**
- Reduced administrative overhead
- Fewer rejected submissions due to clear requirements
- Less back-and-forth communication

### For EAO Staff

**Efficiency Gains:**
- Centralized location for all submissions
- Structured review process
- Reduced manual tracking and coordination
- Faster turnaround times

**Quality:**
- Consistent review process
- Complete information for decision-making
- Ability to track trends and patterns
- Better compliance monitoring

**Accountability:**
- Complete audit trail
- Clear record of decisions and rationale
- Defensible review process

**Resource Management:**
- Better workload visibility
- Ability to prioritize reviews
- Efficient assignment of reviewers

### For the EAO Organization

**Regulatory Excellence:**
- Improved compliance monitoring
- Better enforcement of conditions
- Reduced risk of non-compliance

**Operational Efficiency:**
- Reduced paper-based processes
- Lower administrative costs
- Better resource utilization

**Stakeholder Relations:**
- Improved communication with proponents
- Transparent and fair process
- Enhanced trust and credibility

**Data and Insights:**
- Better data on submission patterns
- Ability to identify systemic issues
- Evidence-based policy improvements

---

## Success Metrics

### Operational Metrics
- Number of submissions processed
- Average time from submission to decision
- Percentage of submissions approved on first review
- User adoption rate

### Quality Metrics
- Submission completeness rate
- Revision request rate
- User satisfaction scores
- System uptime and reliability

### Compliance Metrics
- Percentage of proponents submitting on time
- Compliance with certificate conditions
- Audit trail completeness

---

## Future Enhancements

### Planned Capabilities
- Mobile application for field data collection
- Integration with GIS systems for spatial data
- Advanced analytics and reporting
- Automated compliance checking
- Public transparency portal

### Continuous Improvement
- Regular user feedback collection
- Iterative feature enhancements
- Performance optimization
- User experience improvements

---

*This document provides a business-focused overview of EPIC.submit. For detailed workflows and processes, refer to the companion documents in this series.*
