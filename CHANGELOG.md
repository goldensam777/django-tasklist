# Changelog

All notable changes to the Django Tasklist project will be documented in this file.

## [Unreleased] - 2025-10-23

### Added
- Added comprehensive security settings for HTTPS
- Added HSTS (HTTP Strict Transport Security) support
- Added secure cookie settings (HTTPOnly, Secure flags)
- Added XSS protection headers
- Added clickjacking protection
- Added MIME-type sniffing protection
- Created a detailed CHANGELOG.md
- Added comprehensive README with installation and deployment instructions
- Added environment variable support for sensitive settings

### Changed
- Upgraded Django from 1.6.2 to 4.2.11
- Upgraded Python compatibility to 3.13
- Updated URL patterns to use `path()` instead of `url()`
- Updated imports from `django.core.urlresolvers` to `django.urls`
- Updated `ForeignKey` fields to include `on_delete` parameter
- Replaced `django.contrib.comments` with `django-contrib-comments` package
- Updated project structure to follow modern Django best practices
- Updated requirements.txt with modern, secure package versions

### Removed
- Removed South migrations (replaced with Django's built-in migrations)
- Removed old, unused dependencies
- Removed Python 2.7 compatibility code

### Fixed
- Fixed security vulnerabilities from outdated dependencies
- Fixed URL configuration for Django 4.2 compatibility
- Fixed template context processors configuration
- Fixed static files configuration
- Fixed database migration issues
- Fixed deprecation warnings

### Security
- Enforced HTTPS by default
- Set secure cookie flags
- Enabled CSRF protection
- Added security headers
- Disabled debug mode by default in production settings
- Added proper content security policies

## Migration Notes

### From Django 1.6.2 to 4.2.11
- All URL patterns have been updated to use `path()` instead of `url()`
- The comments framework has been moved to a separate package: `django-contrib-comments`
- Database migrations have been reset - you'll need to recreate your database
- The project now requires Python 3.8 or higher
- The `SECRET_KEY` should now be set via environment variables

### Dependencies
- Added new dependencies:
  - `django-contrib-comments`
  - `whitenoise` for static files
  - `python-dotenv` for environment variable management
- Removed old dependencies:
  - `south`
  - `django-comments` (replaced with `django-contrib-comments`)

### Configuration
- Added `.env.example` for environment variable configuration
- Updated `settings.py` with modern Django settings
- Added security middleware and settings

## [1.0.0] - 2015-03-23
### Added
- Initial release of Django Tasklist
