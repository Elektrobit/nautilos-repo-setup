EBCL - NautilOS Repo Setup
==========================

Provides `ebcl-repo-setup` and `ebc-sync` tools to initialize
credentials protected NautilOS debian repositories from Artifactory.
An environment file `~/.ebcl` is created such that other ebcl tools
can also make use of it.

Tool list:
- ebcl-releases
  Print available release dates
- ebcl-repo-setup
  Setup repository files and update cache
- ebcl-sync
  Fetch for repository release from specific date to local system 
- ebcl-ui
  A dialog guided utility to help the user setup the SDK quickly.