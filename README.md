# BNK48 Member data

This repository contains BNK48 members data in JSON format.

The data is crawled from [BNK48 official website](http://www.bnk48.com).

## Data format

The data is an array of member objects. Each members have the following attributes:

- `thai_first_name` (String): First name in Thai
- `thai_last_name` (String): Last name in Thai
- `english_first_name` (String): First name in English, all caps
- `english_last_name` (String): Last name in English, all caps
- `nickname` (String): Nickname in English
- `birthday` (String): Birthday in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD)
- `height` (int): Height in centimeter
- `province` (String): Origin province
- `like` (Array<String>): Array of item name in string that the member like
- `blood_type` (String): Blood type (A/B/AB/O) of the member
- `hobby`: Hobby of the member
- `facebook` (String): Official Facebook page username. (Hint: add https://www.facebook.com/ prefix to rebuild full URL)
- `instagram` (String): Official Instagram username. (Hint: add https://www.instagram.com/ prefix to rebuild full URL)

The list is sorted as seen on the official website.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, I has waived all copyright and related or neighboring rights to this work.

This data is provided "as is", without warranty of any kind.
