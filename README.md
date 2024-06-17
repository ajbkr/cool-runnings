Cool Runnings
=============

Trivial CPU temperature logging to Adafruit IO for GNU/Linux and macOS.

```
$ cp .env.example .env
```

- `ADAFRUIT_AIO_USERNAME` - Adafruit IO username
- `ADAFRUIT_AIO_KEY` - Adafruit IO key (secret)
- `NAME` - hostname or miner/worker name
- `MACOS` - select platform-specific CPU temperature function, i.e. `True` if running on macOS, else `False`

Cool Runnings logs CPU temperature to a pre-existing Adafruit IO feed named
`NAME-cpu-temperature`. For example, if `NAME=Andrews-MBP`, the program will
will send data to a feed named `andrews-mbp-cpu-temperature`.

NOTE: The value of `NAME` is automatically lower-cased.
