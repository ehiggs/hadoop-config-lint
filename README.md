# Hadoop Config Lint
Too much time is wasted on debugging Hadoop issues due to typos in config.
Enough is enough! Hadoop-config-lint will spot the typos and become part of
your standard tyre kicking checklist for config releases.

# Usage
```
$ hadoop-config-lint 2.6.0 /etc/hadoop
```

# Known issues 
I pulled the config options from the distributed default config xml files that
come with Hadoop. These don't have all the config options. e.g.  On Fedora, I
get 54 options listed as not existing which are in the actual Hadoop source
code.
