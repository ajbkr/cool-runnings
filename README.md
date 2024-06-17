Cool Runnings
=============

Trivial CPU temperature logging to Adafruit IO for GNU/Linux and macOS.

```
$ python3 -m venv .venv
$ . .venv/bin/activate
(.venv) $ pip install -r requirements.txt
```

```
(.venv) $ cp .env.example .env
```

Edit the `.env` file as required. Options include:

- `ADAFRUIT_AIO_USERNAME` - Adafruit IO username
- `ADAFRUIT_AIO_KEY` - Adafruit IO key (secret)
- `NAME` - hostname or miner/worker name
- `MACOS` - select platform-specific CPU temperature function, i.e. `True` if running on macOS, else `False` if running on GNU/Linux

Cool Runnings logs CPU temperature to a pre-existing Adafruit IO feed named
`NAME-cpu-temperature`. For example, if `NAME=Andrews-MBP`, the program will
send data to a feed named `andrews-mbp-cpu-temperature`.

*NOTE: The value of `NAME` is automatically lower-cased.*

```
(.venv) $ ./main.py
```
...or...
```
$ ./run.sh
```

On macOS, to remove the requirement to enter a `sudo` password when
running the program, add the following via `sudo visudo`:

```
%sudo		ALL = (ALL) NOPASSWD: /usr/bin/powermetrics
```
