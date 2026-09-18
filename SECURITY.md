# Security policy

## Supported versions

The project is pre-release. Only the latest commit on the default branch is maintained until the first tagged release.

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability that could expose secrets, enable unauthorized tool use, or affect an upstream dependency. Use GitHub's private vulnerability reporting feature when it is enabled for this repository.

Include:

- affected commit or release;
- reproduction steps;
- expected and observed behaviour;
- potential impact;
- suggested mitigation, if known; and
- whether any real data or credentials may have been exposed.

## Security expectations for contributions

- Never commit real credentials, tokens, certificates, personal information, health information, employer data, or production configurations.
- Demonstration data must be visibly fictional and synthetic.
- New MCP tools must be narrowly scoped and denied by default.
- Generic shell, arbitrary file, unrestricted URL-fetching, and arbitrary database-query tools are prohibited without a new architecture decision and threat-model review.
- Security-relevant behaviour requires tests.
- Dependencies and container images must be pinned before release.
- Logs must avoid raw sensitive values when a hash or redacted value is sufficient.

## Public demonstration safety

Screenshots, recordings, sample reports, and test fixtures must be reviewed for usernames, hostnames, addresses, domains, tokens, document metadata, and other identifying information before publication.
