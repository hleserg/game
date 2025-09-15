# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2025-01-16

### Added
- **Development Tools**: Complete development environment setup
- **EditorConfig**: Unified code style across all editors
- **Pre-commit hooks**: Automated code quality checks with Ruff and MyPy
- **Debug overlay**: Real-time FPS monitoring and game status display
- **Hotkeys**: F1 (toggle overlay), F2 (reset FPS), F3 (fullscreen toggle)
- **Professional workflow**: Make commands for development tasks

### Changed
- Enhanced project structure with comprehensive development tools
- Improved code quality with automated checks
- Better debugging capabilities for game development

### Technical Details
- Ruff for fast linting and formatting
- MyPy for static type checking
- Pre-commit hooks for consistent code quality
- Debug overlay with FPS history and game status
- Professional development workflow

## [1.0.1] - 2025-01-16

### Added
- MIT License
- Comprehensive .gitignore
- MANIFEST.in for distribution
- CHANGELOG.md for version tracking

## [1.0.1] - 2025-01-16

### Added
- Initial release with src/ layout
- PEP 621 compliant pyproject.toml
- Entry point support (`game-collection` command)
- Configuration management with appdirs
- Comprehensive unit tests (85 tests)
- Modern Python tooling (Ruff, MyPy, Pytest)
- CI/CD integration with GitHub Actions
- Four classic arcade games:
  - Snake with growing mechanics
  - Tetris with line clearing
  - Arkanoid with paddle physics
  - Pac-Man with maze navigation

### Changed
- Restructured project to use src/ layout
- Migrated from flat structure to proper package hierarchy
- Updated all imports to use relative imports
- Improved configuration management
- Enhanced score system with platform-specific paths

### Technical Details
- Python 3.10+ support
- Pygame 2.5.0+ dependency
- Appdirs for cross-platform data directories
- Ruff for fast linting and formatting
- MyPy for static type checking
- Pytest for comprehensive testing
- GitHub Actions for CI/CD

## [1.0.0] - 2025-01-15

### Added
- Initial implementation of all four games
- Basic menu system
- Score tracking
- Game logic extraction for testing
- Unit tests for all game logic functions
