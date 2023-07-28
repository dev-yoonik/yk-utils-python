# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## unreleased

## v1.3.5

### Added

- Additional error messages in face authentication class.

## v1.3.4

### Changed

- Error messages in face authentication class.

## v1.3.3

### Changed

- Youverse rebranding.

## v1.3.2

### Added

- Parse error messages in json format in FaceAuthentication class.

## v1.3.1

### Fixed

- Requests wrapper when response is 204 No Content.

## v1.3.0

### Added

- HTTP Request Async Wrapper

## v1.2.0

### Added

- StrBaseEnum class

## v1.1.4

### Added

- BaseEnum class

## v1.1.3

### Added

- Details of quality error messages in Face Authentication class.

## v1.1.2

### Added

- Web Module with URL operations.

### Changed

- More descriptive error messages in Face Authentication class.

## v1.1.1

### Added

- New error code in FaceAuthentication class.

## v1.1.0

### Added

- Error model for API responses.

## v1.0.0

### Added

- Objects module.
- New class to store API result data (instead of proprieties in FaceAuthentication class).

### Changed

- Image module name.
- Read/Write JSON files functions.
- Models deserialization functions.
- FaceAuthentication class to return an ApiResult object on request_face_authentication() method.
- Moved allowed_base64_image() function from FaceAuthentication class to images module.

## v0.2.0

### Added

- New module with utils functions for models.

## v0.1.4

### Fixed

- Setting user attributes in face authentication API request.

## v0.1.3

### Fixed

- Added files module to package build.

## v0.1.2

### Fixed

- Parsing function for error messages.

## v0.1.1

### Fixed

- HTTP requests function for responses different from json type.

## v0.1.0

### Added

- Function to read image and return it as base64 string.
- Function to read configuration files.
- Helpers for APIs: keys, urls and requests handling.
- Wrapper for face authentication API (YooniK Web).
