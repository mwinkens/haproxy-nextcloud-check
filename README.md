# Nextcloud instance check for the haproxy-agent

This repo is a submodule for the [haproxy-agent](https://github.com/mwinkens/haproxy-agent) adding nextcloud specific monitoring information to be polled by the agent.
This allows to automatically adjust agent (and therefore server) weights, if an instance goes for example into maintenance or is offline due to other nextcloud specific reasons.

For example, if one of multiple nextcloud instances goes into maintenance for some reason, the agent sets a weight of 0 and drains users from it.
Of course this software is ment to be used in a scaled environment.

## Installation

- install the [haproxy-agent](https://github.com/mwinkens/haproxy-agent)
- clone this repository anywhere `git clone https://github.com/mwinkens/haproxy-nextcloud-check anywhere`
- link nextcloud_check.py in your haproxy buildins directory (or your `modules`-path for that manner) with
```console
ln -s /path/to/anywhere/nextcloud_check.py /path/to/modules/nextcloud_check.py
```
or just copy it into the modules/buildins path
- make sure `NC_TOKEN` and `NC_URL` are properly set in `haproxy-agent/haproxy-agent.conf` (environment variables).
  - `NC_URL` might usually be `https://127.0.0.1:443` (no trailing slash!)
  - `NC_TOKEN` needs to be generated with `occ config:app:set serverinfo token --value my-fancy-generated-random-token-ABC123`
- restart the haproxy-agent with `systemctl`. You might need a `daemon-reload`

## License

See license

## Author

Marvin Winkens m.winkens@fz-juelich.de
