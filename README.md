# DartFormat

Format dart source code using `dart format`.

### Configuration

Open `Preferences -> Package settings -> DartFormat -> Settings - User`, and edit the settings file using below as a template:

```
{
  "run_on_save": false,
  "dart": "/home/user/bin/dart"
  "args": [
    "--line-length 100"
  ]
}
```

- `run_on_save` - whether to run `dart format` automatically on save. Default is `false`.
- `dart` - path to the dart binary. Default is `"dart"`
- `args` - additional arguments to `dart format`. Default is none.

### Acknowledgement

This plugin is based on [BeautifyRust](https://github.com/vincenting/BeautifyRust).

