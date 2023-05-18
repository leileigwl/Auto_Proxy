import base64


def base64_encode(ctx):  # 将 Url 内容转换为 Base64
    return base64.b64encode(ctx.encode('utf-8')).decode('ascii')


def base64_decode(ctx):
    if '-' in ctx:
        ctx = ctx.replace('-', '+')
    elif '_' in ctx:
        ctx = ctx.replace('_', '/')
    ctx += '=' * (4 - len(ctx) % 4)
    try:
        raw_code = base64.urlsafe_b64decode(ctx.encode('utf-8')).decode('utf-8', 'ignore')
        return raw_code
    except UnicodeDecodeError:
        raise "base64解码出错"

# content1 = 'dm1lc3M6Ly9leUoySWpvZ0lqSWlMQ0FpY0hNaU9pQWlYSFUyTm1ZMFhIVTJOV0l3WEhVMFpUaGxPakExTFRFMUlERTJPakF3SUMxaWVTQkNkVXhwYm1zdWVIbDZMU0JjZFRSbFpUVmNkVFJsTUdKY2RUZ3lPREpjZFRjd1lqbGNkVFJsTUdSY2RUaGlZVEZjZFRaa05ERmNkVGt4WTJZaUxDQWlZV1JrSWpvZ0lseDFOR1kzWmx4MU56VXlPRngxTlRJMFpGeDFPR0ppTUZ4MU5XWTVOMXgxTmpabU5GeDFOalZpTUZ4MU9HSmhNbHgxT1RZd05TSXNJQ0p3YjNKMElqb2dJakFpTENBaWFXUWlPaUFpTm1FelltTmpNRGd0T1dNM055MDBZekF5TFRnME5HSXROR0UyT1RSak5HWXlabVZoSWl3Z0ltRnBaQ0k2SUNJd0lpd2dJbTVsZENJNklDSjBZM0FpTENBaWRIbHdaU0k2SUNKdWIyNWxJaXdnSW1odmMzUWlPaUFpSWl3Z0luQmhkR2dpT2lBaUlpd2dJblJzY3lJNklDSWlmUT09CnRyb2phbjovLzAxZjM0YTA1LWFiMDMtNDY5ZS1iOGVjLTg2YTY5NzYzNTRmYUBzZy5zdGFibGl6ZS50b3A6NDQzI2dpdGh1Yi5jb20vZnJlZWZxJTIwLSUyMCVFNyVCRSU4RSVFNSU5QiVCRCVFNSU4QSVBMCVFNSU4OCVBOSVFNyVBNiU4RiVFNSVCMCVCQyVFNCVCQSU5QSVFNSVCNyU5RSVFNiVCNCU5QiVFNiU5RCU4OSVFNyU5RiVCNkxldmVsMyVFOSU4MCU5QSVFNCVCRiVBMSUyOERJQSUyOSUyMDEKdm1lc3M6Ly9leUoySWpvZ0lqSWlMQ0FpY0hNaU9pQWlaMmwwYUhWaUxtTnZiUzltY21WbFpuRWdMU0JjZFRkbU9HVmNkVFUyWm1RZ0lESWlMQ0FpWVdSa0lqb2dJbUZ6WW1saGMyNWpjeTR4TVRRMU1UUTNPREl1ZUhsNklpd2dJbkJ2Y25RaU9pQWlPRFEwTXlJc0lDSnBaQ0k2SUNJeVl6a3lNRFJrTlMwMU5HSmtMVFJrWkdVdE9ESmxNQzFsT1RrMU5tTmxPVFUwWWpVaUxDQWlZV2xrSWpvZ0lqQWlMQ0FpYm1WMElqb2dJbmR6SWl3Z0luUjVjR1VpT2lBaWJtOXVaU0lzSUNKb2IzTjBJam9nSW5WellYTmlMblkxTUM1dmJtVWlMQ0FpY0dGMGFDSTZJQ0l2ZDJGMVoyWjFhV2QyYUhkdllTSXNJQ0owYkhNaU9pQWlkR3h6SW4wPQp2bWVzczovL2V5SjJJam9nSWpJaUxDQWljSE1pT2lBaVoybDBhSFZpTG1OdmJTOW1jbVZsWm5FZ0xTQmNkVGRtT0dWY2RUVTJabVFnSURNaUxDQWlZV1JrSWpvZ0luVnpZUzV6WlhKMlpYSnlMbk4wYjNKbElpd2dJbkJ2Y25RaU9pQWlNakUyTURjaUxDQWlhV1FpT2lBaU9EQmlNREpsWVRBdE4yRmhNaTAwTkRSbExXSTNZalF0TVRJME5tRTBOemt5T0dJeklpd2dJbUZwWkNJNklDSXdJaXdnSW5OamVTSTZJQ0poZFhSdklpd2dJbTVsZENJNklDSjNjeUlzSUNKMGVYQmxJam9nSW01dmJtVWlMQ0FpYUc5emRDSTZJQ0lpTENBaWNHRjBhQ0k2SUNJdklpd2dJblJzY3lJNklDSjBiSE1pTENBaWMyNXBJam9nSWlJc0lDSmhiSEJ1SWpvZ0lpSjkKdm1lc3M6Ly9leUpoWkdRaU9pQWlZMll1ZVhocWJtOWtaUzVqYjIwaUxDQWlZV2xrSWpvZ0lqQWlMQ0FpYUc5emRDSTZJQ0prY0RNdWVYaHFibTlrWlM1amIyMGlMQ0FpYVdRaU9pQWlNRGxqTVdRek1tUXRORFExT0MwMFpXSm1MV0l6Tm1RdE5HUmtOek15WW1GbE0yRmhJaXdnSW01bGRDSTZJQ0ozY3lJc0lDSndZWFJvSWpvZ0lpOTVlSHBpY0NJc0lDSndiM0owSWpvZ0lqZ3dJaXdnSW5Ceklqb2dJbWRwZEdoMVlpNWpiMjB2Wm5KbFpXWnhJQzBnWEhVM1pqaGxYSFUxTm1aa1EyeHZkV1JHYkdGeVpWeDFPREk0TWx4MU56QmlPU0EwSWl3Z0luTmplU0k2SUNKaGRYUnZJaXdnSW5OdWFTSTZJQ0lpTENBaWRHeHpJam9nSWlJc0lDSjBlWEJsSWpvZ0ltNXZibVVpTENBaWRpSTZJQ0l5SW4wPQp2bWVzczovL2V5SjJJam9nSWpJaUxDQWljSE1pT2lBaVoybDBhSFZpTG1OdmJTOW1jbVZsWm5FZ0xTQmNkVGRtT0dWY2RUVTJabVFnSURVaUxDQWlZV1JrSWpvZ0ltaHJkR0ZrWm5aaUxqRXhORFV4TkRjNE1pNTRlWG9pTENBaWNHOXlkQ0k2SUNJME5ETWlMQ0FpYVdRaU9pQWlNbU01TWpBMFpEVXROVFJpWkMwMFpHUmxMVGd5WlRBdFpUazVOVFpqWlRrMU5HSTFJaXdnSW1GcFpDSTZJQ0l3SWl3Z0ltNWxkQ0k2SUNKM2N5SXNJQ0owZVhCbElqb2dJbTV2Ym1VaUxDQWlhRzl6ZENJNklDSnViRjl1WVhRdWRqVXdMbTl1WlNJc0lDSndZWFJvSWpvZ0lpOTNZWFZuWm5WcFozWm9kMjloSWl3Z0luUnNjeUk2SUNKMGJITWlmUT09CnZtZXNzOi8vZXlKaFpHUWlPaUFpT0RndU1UTTFMalF5TGpJMU1DSXNJQ0oySWpvZ0lqSWlMQ0FpY0hNaU9pQWlaMmwwYUhWaUxtTnZiUzltY21WbFpuRWdMU0JjZFRSbU1HRmNkVFkzTVRjZ0lEWWlMQ0FpY0c5eWRDSTZJREkzTXpNM0xDQWlhV1FpT2lBaVpXSTNNemRpTXpNdFlqYzBOeTAwTW1VNExXTTJZbUV0TnpWaE9XVXdNR0ZrTVdabElpd2dJbUZwWkNJNklDSXdJaXdnSW01bGRDSTZJQ0ozY3lJc0lDSjBlWEJsSWpvZ0lpSXNJQ0pvYjNOMElqb2dJaUlzSUNKd1lYUm9Jam9nSWk5M2MzTXlOek16TnlJc0lDSjBiSE1pT2lBaUluMD0Kdm1lc3M6Ly9leUoySWpvZ0lqSWlMQ0FpY0hNaU9pQWlaMmwwYUhWaUxtTnZiUzltY21WbFpuRWdMU0JjZFRkbU9HVmNkVFUyWm1SRGJHOTFaRVpzWVhKbFhIVTFNVFpqWEhVMU0yWTRRMFJPWEhVNE1qZ3lYSFUzTUdJNUlEY2lMQ0FpWVdSa0lqb2dJbU5tTFdKbGMzUXVkR2xyZEc5clkyeHZkV1F1ZEc5d0lpd2dJbkJ2Y25RaU9pQWlPREE0TUNJc0lDSnBaQ0k2SUNKa01HTmhOMkUzTXkweFl6QXhMVFEyTlRVdE9ERTNaQzB3WWpZMFpUVXhNV0prTUdVaUxDQWlZV2xrSWpvZ0lqQWlMQ0FpYm1WMElqb2dJbmR6SWl3Z0luUjVjR1VpT2lBaWJtOXVaU0lzSUNKb2IzTjBJam9nSW5WekxYVjBMamt4YVhBdWVIbDZJaXdnSW5CaGRHZ2lPaUFpTDJwdWRHMDlNakEwT0NJc0lDSjBiSE1pT2lBaUluMD0Kdm1lc3M6Ly9leUoySWpvZ0lqSWlMQ0FpY0hNaU9pQWlaMmwwYUhWaUxtTnZiUzltY21WbFpuRWdMU0JjZFRkbU9HVmNkVFUyWm1RZ0lEZ2lMQ0FpWVdSa0lqb2dJbU5tTFdOa2JpNTBhV3QwYjJ0amJHOTFaQzUwYjNBaUxDQWljRzl5ZENJNklDSTRNRGd3SWl3Z0ltbGtJam9nSW1Rd1kyRTNZVGN6TFRGak1ERXRORFkxTlMwNE1UZGtMVEJpTmpSbE5URXhZbVF3WlNJc0lDSmhhV1FpT2lBaU1DSXNJQ0p1WlhRaU9pQWlkM01pTENBaWRIbHdaU0k2SUNKdWIyNWxJaXdnSW1odmMzUWlPaUFpY25VdU9URnBjQzU0ZVhvaUxDQWljR0YwYUNJNklDSXZhbTUwYlQweU1EUTRJaXdnSW5Sc2N5STZJQ0lpZlE9PQp2bWVzczovL2V5SmhaR1FpT2lBaU1UQTBMakUzTGpJd01DNHhOamdpTENBaWRpSTZJQ0l5SWl3Z0luQnpJam9nSW1kcGRHaDFZaTVqYjIwdlpuSmxaV1p4SUMwZ1hIVTNaamhsWEhVMU5tWmtRMnh2ZFdSR2JHRnlaVngxTlRFMlkxeDFOVE5tT0VORVRseDFPREk0TWx4MU56QmlPU0E1SWl3Z0luQnZjblFpT2lBME5ETXNJQ0pwWkNJNklDSTRaVE13TnpWaE1DMW1NR0l4TFRFeFpXUXRZall6TkMweU1EVmpObVExWmpWa056Z2lMQ0FpWVdsa0lqb2dJakFpTENBaWJtVjBJam9nSW5keklpd2dJblI1Y0dVaU9pQWlJaXdnSW1odmMzUWlPaUFpYm13dU1ISmtMbTVsZENJc0lDSndZWFJvSWpvZ0lpODFNMjVwYWpRM2VDSXNJQ0owYkhNaU9pQWlkR3h6SW4wPQp2bWVzczovL2V5SjJJam9nSWpJaUxDQWljSE1pT2lBaVoybDBhSFZpTG1OdmJTOW1jbVZsWm5FZ0xTQmNkVFkxWlRWY2RUWTNNbU5jZFRrMk0yWmNkVGt4WTJOY2RUUmxPVEVnTVRBaUxDQWlZV1JrSWpvZ0ltTmtibU5tTG5OamVYVXVZWEJ3SWl3Z0luQnZjblFpT2lBaU9EQTRNQ0lzSUNKcFpDSTZJQ0prTVdaallURTRZaTB3TUdObExUUXdNalF0T0dOak9DMDBZalE1WVRSa1pEVmxOVElpTENBaVlXbGtJam9nSWpBaUxDQWljMk41SWpvZ0ltRjFkRzhpTENBaWJtVjBJam9nSW5keklpd2dJblI1Y0dVaU9pQWlibTl1WlNJc0lDSm9iM04wSWpvZ0luTnpjbk4xWWk1Mk1ESXVjM055YzNWaUxtTnZiU0lzSUNKd1lYUm9Jam9nSWk5aGNHa3Zkak12Wkc5M2JteHZZV1F1WjJWMFJtbHNaU0lzSUNKMGJITWlPaUFpSWl3Z0luTnVhU0k2SUNJaUxDQWlZV3h3YmlJNklDSWlmUT09CnZtZXNzOi8vZXlKaFpHUWlPaUFpYW5Bd01TMWhiSFF0ZG0wd0xtVnVkSEo1TG5OeWRHaGtkeTVoY25RaUxDQWlkaUk2SUNJeUlpd2dJbkJ6SWpvZ0ltZHBkR2gxWWk1amIyMHZabkpsWldaeElDMGdYSFUyTldVMVhIVTJOekpqWEhVMFpURmpYSFUwWldGalFXMWhlbTl1WEhVMk5UY3dYSFUyTXpabFhIVTBaVEprWEhVMVptTXpJREV4SWl3Z0luQnZjblFpT2lBeU1UVTROU3dnSW1sa0lqb2dJakZpWXpVeU16QTRMVEJpWkRrdE16QmtNQzA1TUdaa0xXTmxaak16TnpnM05XUXhNQ0lzSUNKaGFXUWlPaUFpTVNJc0lDSnVaWFFpT2lBaWRHTndJaXdnSW5SNWNHVWlPaUFpSWl3Z0ltaHZjM1FpT2lBaUlpd2dJbkJoZEdnaU9pQWlMeUlzSUNKMGJITWlPaUFpZEd4ekluMD0Kdm1lc3M6Ly9leUoySWpvZ0lqSWlMQ0FpY0hNaU9pQWlaMmwwYUhWaUxtTnZiUzltY21WbFpuRWdMU0JjZFRVek1UZGNkVFJsWVdOY2RUVmxNREpjZFRjNVptSmNkVFV5WVRnZ01USWlMQ0FpWVdSa0lqb2dJak0yTGpFek5DNHhOaTR4T1RBaUxDQWljRzl5ZENJNklDSXhNVEF5TXlJc0lDSnBaQ0k2SUNJNFl6QTBNbUV6T0MwM01XTXhMVEZrWTJJdE1EQmtaaTAxTkRnNE1ESXpObVV3WkdNaUxDQWlZV2xrSWpvZ0lqQWlMQ0FpYzJONUlqb2dJbUYxZEc4aUxDQWlibVYwSWpvZ0luUmpjQ0lzSUNKMGVYQmxJam9nSW01dmJtVWlMQ0FpYUc5emRDSTZJQ0lpTENBaWNHRjBhQ0k2SUNJdklpd2dJblJzY3lJNklDSWlMQ0FpYzI1cElqb2dJaUlzSUNKaGJIQnVJam9nSWlKOQp2bWVzczovL2V5SjJJam9nSWpJaUxDQWljSE1pT2lBaVoybDBhSFZpTG1OdmJTOW1jbVZsWm5FZ0xTQmNkVGRtT0dWY2RUVTJabVJEYkc5MVpFWnNZWEpsWEhVNE1qZ3lYSFUzTUdJNUlERXpJaXdnSW1Ga1pDSTZJQ0l4TnpJdU5qY3VNalEzTGpJMU1DSXNJQ0p3YjNKMElqb2dJamd3SWl3Z0ltbGtJam9nSWpVellXVTJOV0psTFRneFpXVXRORGMyTmkwNFlUQTVMV1JoTkROak5EUmpOR1F6TUNJc0lDSmhhV1FpT2lBaU1DSXNJQ0p6WTNraU9pQWlZWFYwYnlJc0lDSnVaWFFpT2lBaWQzTWlMQ0FpZEhsd1pTSTZJQ0p1YjI1bElpd2dJbWh2YzNRaU9pQWlkWGxoWVM1MmRHTnpjeTUwYjNBaUxDQWljR0YwYUNJNklDSXZjWGRsY2pFeElpd2dJblJzY3lJNklDSWlMQ0FpYzI1cElqb2dJaUlzSUNKaGJIQnVJam9nSWlKOQp2bWVzczovL2V5SjJJam9nSWpJaUxDQWljSE1pT2lBaVoybDBhSFZpTG1OdmJTOW1jbVZsWm5FZ0xTQmNkVGRtT0dWY2RUVTJabVFnSURFMElpd2dJbUZrWkNJNklDSnFjSGRoWkc1allTNHhNVFExTVRRM09ESXVlSGw2SWl3Z0luQnZjblFpT2lBaU1qQTVOaUlzSUNKcFpDSTZJQ0l5WXpreU1EUmtOUzAxTkdKa0xUUmtaR1V0T0RKbE1DMWxPVGsxTm1ObE9UVTBZalVpTENBaVlXbGtJam9nSWpBaUxDQWlibVYwSWpvZ0luZHpJaXdnSW5SNWNHVWlPaUFpYm05dVpTSXNJQ0pvYjNOMElqb2dJbXh6ZDJwekxuWTFNQzV2Ym1VaUxDQWljR0YwYUNJNklDSXZkMkYxWjJaMWFXZDJhSGR2WVNJc0lDSjBiSE1pT2lBaWRHeHpJbjA9CnZtZXNzOi8vZXlKMklqb2dJaklpTENBaWNITWlPaUFpWjJsMGFIVmlMbU52YlM5bWNtVmxabkVnTFNCY2RUazVPVGxjZFRabE1tWmNkVGN5TnpsY2RUVXlNbUpjZFRnNE5HTmNkVFkxTTJaY2RUVXpNMkVnTVRVaUxDQWlZV1JrSWpvZ0lqSXdNaTQ0TVM0eU16RXVNVFV3SWl3Z0luQnZjblFpT2lBaU9EQWlMQ0FpYVdRaU9pQWlNV1F4WXpGa09UUXROams0TnkwME5qVTRMV0UwWkdNdE9EZ3lNV0V6TUdabE4yVXdJaXdnSW1GcFpDSTZJQ0l3SWl3Z0luTmplU0k2SUNKaGRYUnZJaXdnSW01bGRDSTZJQ0ozY3lJc0lDSjBlWEJsSWpvZ0ltNXZibVVpTENBaWFHOXpkQ0k2SUNKcFpHNTFjMkZ1WlhRdWRuQnVaWGhsWTNWMGFYWmxMbTE1TG1sa0lpd2dJbkJoZEdnaU9pQWlMeUlzSUNKMGJITWlPaUFpSWl3Z0luTnVhU0k2SUNJaUxDQWlZV3h3YmlJNklDSWlmUT09CnZtZXNzOi8vZXlKMklqb2dJaklpTENBaWNITWlPaUFpWjJsMGFIVmlMbU52YlM5bWNtVmxabkVnTFNCY2RUZG1PR1ZjZFRVMlptUWdJREUySWl3Z0ltRmtaQ0k2SUNJeE9USXVNakF6TGpJek1DNDROaUlzSUNKd2IzSjBJam9nSWpnd0lpd2dJbWxrSWpvZ0ltRTBOREprWVdObUxXTmlZak10TkRnNFlTMDVOelEwTFRZeE5EazBaV0V6T0RZek1DSXNJQ0poYVdRaU9pQWlNQ0lzSUNKelkza2lPaUFpWVhWMGJ5SXNJQ0p1WlhRaU9pQWlkM01pTENBaWRIbHdaU0k2SUNKdWIyNWxJaXdnSW1odmMzUWlPaUFpZFhNdE1TNWhZM2wxYmk1alppSXNJQ0p3WVhSb0lqb2dJaThpTENBaWRHeHpJam9nSWlJc0lDSnpibWtpT2lBaUlpd2dJbUZzY0c0aU9pQWlJbjA9CnZtZXNzOi8vZXlKb2IzTjBJam9nSWlJc0lDSndZWFJvSWpvZ0lpOXNiMjlySWl3Z0luQnZjblFpT2lBaU5EUXpJaXdnSW5Sc2N5STZJQ0owYkhNaUxDQWljSE1pT2lBaVoybDBhSFZpTG1OdmJTOW1jbVZsWm5FZ0xTQmNkVGRtT0dWY2RUVTJabVJEYkc5MVpFWnNZWEpsWEhVMU1UWmpYSFUxTTJZNFEwUk9YSFU0TWpneVhIVTNNR0k1SURFM0lpd2dJbWxrSWpvZ0ltWTNZalppWVRFeUxXWXlaRFF0TVRGbFpDMWlPVGM1TFRBd01EQXhOekF5TWpBd09DSXNJQ0poWkdRaU9pQWlZV0ZoWVM1M2VIZ3VaMkY1SWl3Z0luWWlPaUFpTWlJc0lDSmhhV1FpT2lBaU1DSXNJQ0p1WlhRaU9pQWlkM01pTENBaWRIbHdaU0k2SUNKdWIyNWxJbjA9CnZtZXNzOi8vZXlKMklqb2dJaklpTENBaWNITWlPaUFpWjJsMGFIVmlMbU52YlM5bWNtVmxabkVnTFNCY2RUZG1PR1ZjZFRVMlptUkRiRzkxWkVac1lYSmxYSFUxTVRaalhIVTFNMlk0UTBST1hIVTRNamd5WEhVM01HSTVLSE5vYjNCcFpua3BJREU0SWl3Z0ltRmtaQ0k2SUNJeU15NHlNamN1TXpndU9Ua2lMQ0FpY0c5eWRDSTZJQ0kwTkRNaUxDQWlhV1FpT2lBaU9EWmtNemMxTWpZdE5UYzFPQzAwWTJWakxUZzJNbVl0WkdZME1EUmlNekV6TURnMklpd2dJbUZwWkNJNklDSXdJaXdnSW5OamVTSTZJQ0poZFhSdklpd2dJbTVsZENJNklDSjNjeUlzSUNKMGVYQmxJam9nSW01dmJtVWlMQ0FpYUc5emRDSTZJQ0l4TG1aeVpXVnJNUzU0ZVhvaUxDQWljR0YwYUNJNklDSXZNMGMyVjFCRVREY2lMQ0FpZEd4eklqb2dJblJzY3lJc0lDSnpibWtpT2lBaUlpd2dJbUZzY0c0aU9pQWlJbjA9CnZtZXNzOi8vZXlKMklqb2dJaklpTENBaWNITWlPaUFpWjJsMGFIVmlMbU52YlM5bWNtVmxabkVnTFNCY2RUZG1PR1ZjZFRVMlptUkRiRzkxWkVac1lYSmxYSFUxTVRaalhIVTFNMlk0UTBST1hIVTRNamd5WEhVM01HSTVJREU1SWl3Z0ltRmtaQ0k2SUNKMFpXTm9MbTV2WVhKcFpYTXVaR1VpTENBaWNHOXlkQ0k2SUNJNE1DSXNJQ0pwWkNJNklDSXlaRFZrT0dJNVl5MDRaV00wTFRSaE16Y3RZall4TUMwM09HVTNNV1V4TTJWaFpXWWlMQ0FpWVdsa0lqb2dJakFpTENBaWMyTjVJam9nSW1GMWRHOGlMQ0FpYm1WMElqb2dJbmR6SWl3Z0luUjVjR1VpT2lBaWJtOXVaU0lzSUNKb2IzTjBJam9nSW01c0xuTm9ZWEpsWTJWdWRISmxjSEp2TG1OdmJTSXNJQ0p3WVhSb0lqb2dJaTl6YUdseWEyVnlJaXdnSW5Sc2N5STZJQ0lpTENBaWMyNXBJam9nSWlJc0lDSmhiSEJ1SWpvZ0lpSjkKdm1lc3M6Ly9leUoySWpvZ0lqSWlMQ0FpY0hNaU9pQWlaMmwwYUhWaUxtTnZiUzltY21WbFpuRWdMU0JjZFRkbU9HVmNkVFUyWm1SY2RUVXlZVEJjZFRVeU1qbGNkVGM1T0daY2RUVmpNMk5jZFRSbE9XRmNkVFZrWkdWY2RUVTNNak5jZFRSbU5UVmNkVFU0TldWRGJHOTFaR1pzWVhKbFEwUk9YSFU0TWpneVhIVTNNR0k1SURJd0lpd2dJbUZrWkNJNklDSXhNRE11TWpFdU1qUTBMak0zSWl3Z0luQnZjblFpT2lBaU9EQWlMQ0FpYVdRaU9pQWlOVE5oWlRZMVltVXRPREZsWlMwME56WTJMVGhoTURrdFpHRTBNMk0wTkdNMFpETXdJaXdnSW1GcFpDSTZJQ0l3SWl3Z0luTmplU0k2SUNKaGRYUnZJaXdnSW01bGRDSTZJQ0ozY3lJc0lDSjBlWEJsSWpvZ0ltNXZibVVpTENBaWFHOXpkQ0k2SUNKMWVXRmhMblowWTNOekxuUnZjQ0lzSUNKd1lYUm9Jam9nSWk5eGQyVnlNVEVpTENBaWRHeHpJam9nSWlJc0lDSnpibWtpT2lBaUlpd2dJbUZzY0c0aU9pQWlJbjA9CnZtZXNzOi8vZXlKMklqb2dJaklpTENBaWNITWlPaUFpWjJsMGFIVmlMbU52YlM5bWNtVmxabkVnTFNCY2RUVXpNVGRjZFRSbFlXTmNkVFZsTURKY2RUYzVabUpjZFRVeVlUZ2dNakVpTENBaVlXUmtJam9nSWpNMkxqRXpOQzR4Tmk0eE56RWlMQ0FpY0c5eWRDSTZJQ0l4TVRBeU15SXNJQ0pwWkNJNklDSTRZekEwTW1Fek9DMDNNV014TFRGa1kySXRNREJrWmkwMU5EZzRNREl6Tm1Vd1pHTWlMQ0FpWVdsa0lqb2dJakFpTENBaWMyTjVJam9nSW1GMWRHOGlMQ0FpYm1WMElqb2dJblJqY0NJc0lDSjBlWEJsSWpvZ0ltNXZibVVpTENBaWFHOXpkQ0k2SUNJaUxDQWljR0YwYUNJNklDSXZJaXdnSW5Sc2N5STZJQ0lpTENBaWMyNXBJam9nSWlJc0lDSmhiSEJ1SWpvZ0lpSjkKdHJvamFuOi8vOTQ3OGUyN2MtNmJkZC00ZjBlLWJhNDYtOTBkOTczOWUxZTM0QHVrLnN0YWJsaXplLnRvcDo0NDMjZ2l0aHViLmNvbS9mcmVlZnElMjAtJTIwJUU3JUJFJThFJUU1JTlCJUJEJUU1JThBJUEwJUU1JTg4JUE5JUU3JUE2JThGJUU1JUIwJUJDJUU0JUJBJTlBJUU1JUI3JTlFJUU2JUI0JTlCJUU2JTlEJTg5JUU3JTlGJUI2TGV2ZWwzJUU5JTgwJTlBJUU0JUJGJUExJTI4RElBJTI5JTIwMjIKdm1lc3M6Ly9leUoySWpvZ0lqSWlMQ0FpY0hNaU9pQWlaMmwwYUhWaUxtTnZiUzltY21WbFpuRWdMU0JjZFRkbU9HVmNkVFUyWm1SRGJHOTFaRVpzWVhKbFhIVTRNamd5WEhVM01HSTVJREl6SWl3Z0ltRmtaQ0k2SUNKalppMXNkQzV6YUdGeVpXTmxiblJ5WlM1dmJteHBibVVpTENBaWNHOXlkQ0k2SUNJNE1EZ3dJaXdnSW1sa0lqb2dJbVF4Wm1OaE1UaGlMVEF3WTJVdE5EQXlOQzA0WTJNNExUUmlORGxoTkdSa05XVTFNaUlzSUNKaGFXUWlPaUFpTUNJc0lDSnpZM2tpT2lBaVlYVjBieUlzSUNKdVpYUWlPaUFpZDNNaUxDQWlkSGx3WlNJNklDSnViMjVsSWl3Z0ltaHZjM1FpT2lBaWMzTnljM1ZpTG5Zd01TNXpjM0p6ZFdJdVkyOXRJaXdnSW5CaGRHZ2lPaUFpTDJGd2FTOTJNeTlrYjNkdWJHOWhaQzVuWlhSR2FXeGxJaXdnSW5Sc2N5STZJQ0lpTENBaWMyNXBJam9nSWlKOQo'
# content2 = 'eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTdmOGVcdTU2ZmQgIDUiLCAiYWRkIjogImhrdGFkZnZiLjExNDUxNDc4Mi54eXoiLCAicG9ydCI6ICI0NDMiLCAiaWQiOiAiMmM5MjA0ZDUtNTRiZC00ZGRlLTgyZTAtZTk5NTZjZTk1NGI1IiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ3cyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJubF9uYXQudjUwLm9uZSIsICJwYXRoIjogIi93YXVnZnVpZ3Zod29hIiwgInRscyI6ICJ0bHMifQ=='
# res = base64_decode(content2)
# print(res)
