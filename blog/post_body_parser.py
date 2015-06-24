# -*- coding: utf-8 -*-

import re
import markdown2


def parse_blocks(raw_post_body):
    lines = raw_post_body.split("\n")
    blocks = []

    current_block_name, current_block_body = None, u""

    for l in lines:
        line = l.replace("\r", "").strip()

        r = re.match("\[\[\s*(\w+)\s*\]\]", line)
        if r is None:
            current_block_body += u"%s\n" % line

        else:
            if current_block_name:  # save previous block
                blocks.append((current_block_name.upper(), current_block_body))
            current_block_name, current_block_body = r.groups()[0], u""

    if current_block_name:
        blocks.append((current_block_name.upper(), current_block_body))

    if not blocks:
        blocks.append(("TEXT", raw_post_body))

    return blocks


def parse_markdown(block_body):
    return markdown2.markdown(block_body)


def parse_text(block_body):
    lines = block_body.split("\n")
    parsed_text = u""

    for l in lines:
        line = l.replace("\r", "")

        parsed_text += u"<p>%s</p>\n" % line

    return parsed_text


BLOCK_PARSER = {
    "MARKDOWN": parse_markdown,
    "TEXT": parse_text,
    "CODE": lambda x: "<pre>%s</pre>" % x,
}


def parse(raw_post_body):
    blocks = parse_blocks(raw_post_body)
    body_str = u""

    for block in blocks:
        if block[0] in BLOCK_PARSER:
            body_str += u"\n%s\n" % unicode(BLOCK_PARSER[block[0]](block[1]))
        else:
            body_str += u"\n%s\n" % unicode(block[1])

    return body_str


