<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes" />

    <xsl:template match="/">
        <html>
            <head>
                <title>
                    <xsl:value-of select="rss/channel/title" />
                </title>
                <style>
                    body { font-family: Arial, sans-serif; }
                    h1 { color: #333; text-align:center; margin-bottom:0;}
                    ul { list-style-type: none; padding: 0; }
                    li { margin-bottom: 20px; }
                    a { text-decoration: none; color: #0066cc; }
                    p { color: #666;}
                    .subhead {text-align:center;}
                    li {margin: 1em 0 1em 0;}
                    li * {line-height:1; margin: 0 0 0 1em;}
                </style>
            </head>
            <body>
                <h1>
                    <xsl:value-of select="rss/channel/title" />
                </h1>
                <p class='subhead'>
                    <xsl:value-of select="rss/channel/description"  disable-output-escaping="no"/>
                </p>
                <ul>
                    <xsl:for-each select="rss/channel/item">
                        <li>
                            <a href="{link}">
                                <xsl:value-of select="title" />
                            </a>
                            <p>
                                <xsl:value-of select="description" disable-output-escaping="no"/>
                            </p>
                            <p>
                                <xsl:value-of select="pubDate" />
                            </p>
                        </li>
                    </xsl:for-each>
                </ul>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>