username=$1
crt=$2
key=$3

touch vpn/confvpn/$username.ovpn

echo "client
tls-client
pull
dev tun
proto udp4
remote erwansinck.fr 1194
resolv-retry infinite
nobind
#user nobody
#group nogroup
persist-key
persist-tun
key-direction 1
remote-cert-tls server
auth-nocache
comp-lzo
verb 3
auth SHA512
<tls-auth>
#
# 2048 bit OpenVPN static key
#
-----BEGIN OpenVPN Static key V1-----
107bb200b9668fcca571580997b34518
1bee63729ebb085075833d9de25a2ff0
206b5528a0f80328709e51b53dd6e20e
b5db07c0ebde25c4b9c5b10ccfb8afea
cb1f03978567213d88fd8415fb60aa5d
b0d2fbde1be33533decbfb1fce6101fc
f16357b1fbd140c1e8dd375ed7c8a2d5
448e28adee53ddf45e49df79f39a7f9a
0ab46fbee670c0302cf96747d62e7775
c6e063a393bd444d55973e8471c17186
ac153ff278a761031dcb6a9f90847b86
a0bd57dc7e95143c34a58e2bef29ae6d
5f2186afdb36a970a712dacec2d194c5
78226ef470ae617a6df57eba4e2728f7
138683b66cfe120dfba527df551c5f5d
7eae8c611f06fbc2fb4bb55556a19dd0
-----END OpenVPN Static key V1-----
</tls-auth>
<ca>
-----BEGIN CERTIFICATE-----
MIIDVzCCAj+gAwIBAgIUR3hBoVA97A+yKWxbvtZ14OKZgWMwDQYJKoZIhvcNAQEL
BQAwGjEYMBYGA1UEAwwPVnBuIEVyd2FuIFNJTkNLMB4XDTI0MDUxNDEzNTU0N1oX
DTM0MDUxMjEzNTU0N1owGjEYMBYGA1UEAwwPVnBuIEVyd2FuIFNJTkNLMIIBIjAN
BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvfWRGzBGGDIEyZWVt8xMtXi3zKpC
AKaaroLQ+woTy9igWQnlKyF6eQavmBjR6oFaAycrkgHft5iI1otWsRC/gkaMv7Og
0zSx8xyC4MXC52pLkmavs0kePoEMHlt3RLNSNUmdmJMc+3S1+B9VnYgWNU2VXlaj
JJUw33DF36IGkhln+ozvpqe6Hs69yXFiik9lHbyym3mE45IczB+FhI5SYG3DfGXW
6Ro7xsVOXtwo0vG8zOROrUc6LpVQQSXDsoDVLxdSPGB3OCCgBxQTUzlQyRzvKi+O
dl81I1G6LuDEIJUAq6OkThkYy+ElAxDO/7Gvqw7OiYRWD5uy5iO2ExF+NQIDAQAB
o4GUMIGRMB0GA1UdDgQWBBTZ8GFciSt49SJJT5IFUYebpqjtczBVBgNVHSMETjBM
gBTZ8GFciSt49SJJT5IFUYebpqjtc6EepBwwGjEYMBYGA1UEAwwPVnBuIEVyd2Fu
IFNJTkNLghRHeEGhUD3sD7IpbFu+1nXg4pmBYzAMBgNVHRMEBTADAQH/MAsGA1Ud
DwQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAkPpVzGi1fWmKHU0L784s0sAPxQ70
lkPyhMtk4yJrG0v1WmQUzbrU071mpmyUha5HFCRjqXUJGYyC3LOCbs+1IdyuhRKf
i1v0ChlJYkkoTveBcuA9B7/01qwJI2I9lcs6SG1uaKgXS/UjY6Hm3e3LWeKmRm2h
pxLycxS+VUDhMRPzbZ3gmW3IXxgwtQDp8DcsD8djUk4MaagbC1d2fdzkmtxOXPfm
cRJR7D3o/HvvjvDY5665wXl0F4rAG+SFq3UQOlLJQex9Gu6nLf820MJlOJyaNGev
HookmvDoeddzMCv9oH9/+fNhiarxtxza8jdKClJ74/RsbpOhGRyN15FwgQ==
-----END CERTIFICATE-----
</ca>
<cert>
$crt
</cert>
<key>
$key
</key>" >> vpn/confvpn/$username.ovpn