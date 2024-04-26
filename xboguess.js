// 引入 CryptoJS 库
var md5 = require("md5");


function getXBogus(params, data, userAgent) {
    // 生成乱码字符串
    var garbledString = getGarbledString(params, data, userAgent);
    let short_str = "Dkdpgh4ZKsQB80/Mfvw36XI1R25-WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe="
    var XBogus = "";
    // 依次生成七组字符串
    for (var i = 0; i <= 20; i += 3) {
        var charCodeAtNum0 = garbledString.charCodeAt(i);
        var charCodeAtNum1 = garbledString.charCodeAt(i + 1);
        var charCodeAtNum2 = garbledString.charCodeAt(i + 2);
        var baseNum = charCodeAtNum2 | charCodeAtNum1 << 8 | charCodeAtNum0 << 16;
        // 依次生成四个字符
        var str1 = short_str[(baseNum & 16515072) >> 18];
        var str2 = short_str[(baseNum & 258048) >> 12];
        var str3 = short_str[(baseNum & 4032) >> 6];
        var str4 = short_str[baseNum & 63];
        XBogus += str1 + str2 + str3 + str4;
    }
    return XBogus;
}

function getGarbledString(params, data, userAgent) {
    let fixedString1 = new Date().getTime() / 1000;
    let fixedString2 = 2421646185;
    // let  num = [64, 1, 20, 46, 4, 0, 0, 144, 99, 77, 0.00390625, 8, 71, 13, 189, 0, 0, 87, 105]
    let  num = get_arr(fixedString1,fixedString2,params,data,userAgent)
    return garbledCharacters(num);
}

function get_arr(timestamp1,timestamp2,params,data,userAgent){
    let uaGarbled = _0x25788b.apply(null,[_0x5caed2.apply(null,[1,8]),userAgent]);
    let uaStr = _0x1f3b8d(md5(ua(userAgent).toString()));
    let paramsarr1 = _0x1f3b8d(md5(_0x1f3b8d(md5(params).toString())).toString());
    let dataArr2 = _0x1f3b8d(md5((_0x1f3b8d(md5(data).toString()))).toString());
    var arr = [];
    arr[0] = 64;
    arr[1] = 0.00390625;
    arr[2] = 1;
    arr[3] = 8;
    arr[4] = paramsarr1[14];
    arr[5] = paramsarr1[15];
    arr[6] = dataArr2[14];
    arr[7] = dataArr2[15];
    arr[8] = uaStr[14];
    arr[9] = uaStr[15];
    arr[10] = timestamp1 >> 24 & 255;
    arr[11] = timestamp1 >> 16 & 255;
    arr[12] = timestamp1 >> 8 & 255;
    arr[13] = timestamp1 >> 0 & 255;
    arr[14] = timestamp2 >> 24 & 255;
    arr[15] = timestamp2 >> 16 & 255;
    arr[16] = timestamp2 >> 8 & 255;
    arr[17] = timestamp2 >> 0 & 255;
    const xorResult = arr.reduce(function(a, b) { return a ^ b; });
    arr[18] = xorResult;
    arr[19] = 255;
    return array2 = [arr[0], arr[2], arr[4], arr[6], arr[8], arr[10], arr[12], arr[14], arr[16], arr[18], arr[1], arr[3], arr[5], arr[7], arr[9], arr[11], arr[13], arr[15], arr[17]];
}

_0x1f3b8d = function(a) {
    _0x19ae48 = [null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0,1,2,3,4,5,6,7,8,9,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,10,11,12,13,14,15]
    for (var b = a.length >> 1, c = b << 1, e = new Uint8Array(b), d = 0, t = 0; t < c;) {
        e[d++] = _0x19ae48[a.charCodeAt(t++)] << 4 | _0x19ae48[a.charCodeAt(t++)];
    }
    return e;
}

function ua(userAgent) {
  return _0x38c772.apply(null,[_0x25788b.apply(null,[_0x5caed2.apply(null,[1,8]),userAgent]), 's0'])
}

function _0x5caed2(a, b) {
    var c = new Uint8Array(3);
    return c[0] = a / 256, c[1] = a % 256, c[2] = b % 256, String.fromCharCode.apply(null, c);
}

function garbledCharacters(num) {
    return _0x94582.apply(null,[2,255,_0x25788b.apply(null,['ÿ', _0x398111.apply(null, num)])])
}

function _0x86cb82(a) {
    return String.fromCharCode(a);
}

function _0x94582(a, b, c) {
    return _0x86cb82(a) + _0x86cb82(b) + c;
}
function _0x25788b(a, b) {
    for (var c, e = [], d = 0, t = "", f = 0; f < 256; f++) {
        e[f] = f;
    }
    for (var r = 0; r < 256; r++) {
        d = (d + e[r] + a.charCodeAt(r % a.length)) % 256, c = e[r], e[r] = e[d], e[d] = c;
    }
    var n = 0;
    d = 0;
    for (var o = 0; o < b.length; o++) {
        d = (d + e[n = (n + 1) % 256]) % 256, c = e[n], e[n] = e[d], e[d] = c, t += String.fromCharCode(b.charCodeAt(o) ^ e[(e[n] + e[d]) % 256]);
    }
    return t;
}

function _0x398111(a, b, c, e, d, t, f, r, n, o, i, _, x, u, s, l, v, h, p) {
    var y = new Uint8Array(19);
    return y[0] = a, y[1] = i, y[2] = b, y[3] = _, y[4] = c, y[5] = x, y[6] = e, y[7] = u,
        y[8] = d, y[9] = s, y[10] = t, y[11] = l, y[12] = f, y[13] = v, y[14] = r, y[15] = h,
        y[16] = n, y[17] = p, y[18] = o, String.fromCharCode.apply(null, y);
}

function jsvmp(a, b, c) {
    function e() {
        if ("undefined" == typeof Reflect || !Reflect.construct) {
            return !1;
        }
        if (Reflect.construct.sham) {
            return !1;
        }
        if ("function" == typeof Proxy) {
            return !0;
        }
        try {
            return Date.prototype.toString.call(Reflect.construct(Date, [], function() {})),
            !0;
        } catch (a) {
            return !1;
        }
    }
    function d(a, b, c) {
        return (d = e() ? Reflect.construct : function(a, b, c) {
            var e = [ null ];
            e.push.apply(e, b);
            var d = new (Function.bind.apply(a, e))();
            return c && t(d, c.prototype), d;
        }).apply(null, arguments);
    }
    function t(a, b) {
        return (t = Object.setPrototypeOf || function(a, b) {
            return a.__proto__ = b, a;
        })(a, b);
    }
    function f(a) {
        return function(a) {
            if (Array.isArray(a)) {
                for (var b = 0, c = new Array(a.length); b < a.length; b++) {
                    c[b] = a[b];
                }
                return c;
            }
        }(a) || function(a) {
            if (Symbol.iterator in Object(a) || "[object Arguments]" === Object.prototype.toString.call(a)) {
                return Array.from(a);
            }
        }(a) || function() {
            throw new TypeError("Invalid attempt to spread non-iterable instance");
        }();
    }
    for (var r = [], n = 0, o = [], i = 0, _ = function(a, b) {
        var c = a[b++], e = a[b], d = parseInt("" + c + e, 16);
        if (d >> 7 == 0) {
            return [ 1, d ];
        }
        if (d >> 6 == 2) {
            var t = parseInt("" + a[++b] + a[++b], 16);
            return d &= 63, [ 2, t = (d <<= 8) + t ];
        }
        if (d >> 6 == 3) {
            var f = parseInt("" + a[++b] + a[++b], 16), r = parseInt("" + a[++b] + a[++b], 16);
            return d &= 63, [ 3, r = (d <<= 16) + (f <<= 8) + r ];
        }
    }, x = function(a, b) {
        var c = parseInt("" + a[b] + a[b + 1], 16);
        return c > 127 ? -256 + c : c;
    }, u = function(a, b) {
        var c = parseInt("" + a[b] + a[b + 1] + a[b + 2] + a[b + 3], 16);
        return c > 32767 ? -65536 + c : c;
    }, s = function(a, b) {
        var c = parseInt("" + a[b] + a[b + 1] + a[b + 2] + a[b + 3] + a[b + 4] + a[b + 5] + a[b + 6] + a[b + 7], 16);
        return c > 2147483647 ? 0 + c : c;
    }, l = function(a, b) {
        return parseInt("" + a[b] + a[b + 1], 16);
    }, v = function(a, b) {
        return parseInt("" + a[b] + a[b + 1] + a[b + 2] + a[b + 3], 16);
    }, h = h || this || window, p = (Object.keys, a.length, 0), y = "", g = p; g < p + 16; g++) {
        var w = "" + a[g++] + a[g];
        w = parseInt(w, 16), y += String.fromCharCode(w);
    }
    if ("HNOJ@?RC" != y) {
        throw new Error("error magic number " + y);
    }
    p += 16, parseInt("" + a[p] + a[p + 1], 16), p += 8, n = 0;
    for (var m = 0; m < 4; m++) {
        var O = p + 2 * m, S = "" + a[O++] + a[O], E = parseInt(S, 16);
        n += (3 & E) << 2 * m;
    }
    p += 16, p += 8;
    var T = parseInt("" + a[p] + a[p + 1] + a[p + 2] + a[p + 3] + a[p + 4] + a[p + 5] + a[p + 6] + a[p + 7], 16), A = T, C = p += 8, j = v(a, p += T);
    j[1], p += 4, r = {
        p: [],
        q: []
    };
    for (var P = 0; P < j; P++) {
        for (var k = _(a, p), I = p += 2 * k[0], R = r.p.length, M = 0; M < k[1]; M++) {
            var D = _(a, I);
            r.p.push(D[1]), I += 2 * D[0];
        }
        p = I, r.q.push([ R, r.p.length ]);
    }
    var U = {
        5: 1,
        6: 1,
        70: 1,
        22: 1,
        23: 1,
        37: 1,
        73: 1
    }, N = {
        72: 1
    }, B = {
        74: 1
    }, z = {
        11: 1,
        12: 1,
        24: 1,
        26: 1,
        27: 1,
        31: 1
    }, X = {
        10: 1
    }, L = {
        2: 1,
        29: 1,
        30: 1,
        20: 1
    }, V = [], F = [];
    function q(a, b, c) {
        for (var e = b; e < b + c; ) {
            var d = l(a, e);
            V[e] = d, e += 2, N[d] ? (F[e] = x(a, e), e += 2) : U[d] ? (F[e] = u(a, e), e += 4) : B[d] ? (F[e] = s(a, e),
            e += 8) : z[d] ? (F[e] = l(a, e), e += 2) : X[d] ? (F[e] = v(a, e), e += 4) : L[d] && (F[e] = v(a, e),
            e += 4);
        }
    }
    return $(a, C, A / 2, [], b, c);
    function W(a, b, c, e, t, _, p, y) {
        null == _ && (_ = this);
        var g, w, m, O = [], S = 0;
        p && (g = p);
        var E, T, A = b, C = A + 2 * c;
        if (!y) {
            for (;A < C; ) {
                var j = parseInt("" + a[A] + a[A + 1], 16);
                A += 2;
                var P = 3 & (E = 13 * j % 241);
                if (E >>= 2, P < 1) {
                    P = 3 & E;
                    if (E >>= 2, P > 2) {
                        (P = E) < 1 ? O[++S] = null : P < 3 ? (g = O[S--], O[S] = O[S] >= g) : P < 12 && (O[++S] = void 0);
                    } else if (P > 1) {
                        if ((P = E) < 9) {
                            for (g = O[S--], T = v(a, A), P = "", M = r.q[T][0]; M < r.q[T][1]; M++) {
                                P += String.fromCharCode(n ^ r.p[M]);
                            }
                            A += 4, O[S--][P] = g;
                        } else if (P < 13) {
                            throw O[S--];
                        }
                    } else if (P > 0) {
                        (P = E) > 8 ? (g = O[S--], O[S] = typeof g) : P > 4 ? O[S -= 1] = O[S][O[S + 1]] : P > 2 && (w = O[S--],
                        (P = O[S]).x === W ? P.y >= 1 ? O[S] = $(a, P.c, P.l, [ w ], P.z, m, null, 1) : (O[S] = $(a, P.c, P.l, [ w ], P.z, m, null, 0),
                        P.y++) : O[S] = P(w));
                    } else if ((P = E) > 14) {
                        T = u(a, A), (k = function b() {
                            var c = arguments;
                            return b.y > 0 ? $(a, b.c, b.l, c, b.z, this, null, 0) : (b.y++, $(a, b.c, b.l, c, b.z, this, null, 0));
                        }).c = A + 4, k.l = T - 2, k.x = W, k.y = 0, k.z = t, O[S] = k, A += 2 * T - 2;
                    } else if (P > 12) {
                        w = O[S--], m = O[S--], (P = O[S--]).x === W ? P.y >= 1 ? O[++S] = $(a, P.c, P.l, w, P.z, m, null, 1) : (O[++S] = $(a, P.c, P.l, w, P.z, m, null, 0),
                        P.y++) : O[++S] = P.apply(m, w);
                    } else if (P > 5) {
                        g = O[S--], O[S] = O[S] != g;
                    } else if (P > 3) {
                        g = O[S--], O[S] = O[S] * g;
                    } else if (P > -1) {
                        return [ 1, O[S--] ];
                    }
                } else if (P < 2) {
                    P = 3 & E;
                    if (E >>= 2, P > 2) {
                        if ((P = E) > 12) {
                            O[++S] = _;
                        } else if (P > 5) {
                            g = O[S--], O[S] = O[S] !== g;
                        } else if (P > 3) {
                            g = O[S--], O[S] = O[S] / g;
                        } else if (P > 1) {
                            if ((T = u(a, A)) < 0) {
                                y = 1, q(a, b, 2 * c), A += 2 * T - 2;
                                break;
                            }
                            A += 2 * T - 2;
                        } else {
                            P > -1 && (O[S] = !O[S]);
                        }
                    } else if (P > 1) {
                        (P = E) > 11 ? (g = O[S], O[++S] = g) : P > 9 ? (g = O[S -= 2][O[S + 1]] = O[S + 2],
                        S--) : P > 0 && (O[++S] = g);
                    } else if (P > 0) {
                        if ((P = E) > 12) {
                            O[++S] = x(a, A), A += 2;
                        } else if (P > 10) {
                            g = O[S--], O[S] = O[S] << g;
                        } else if (P > 8) {
                            for (T = v(a, A), P = "", M = r.q[T][0]; M < r.q[T][1]; M++) {
                                P += String.fromCharCode(n ^ r.p[M]);
                            }
                            A += 4, O[S] = O[S][P];
                        } else {
                            P > 6 && (w = O[S--], g = delete O[S--][w]);
                        }
                    } else if ((P = E) < 5) {
                        T = u(a, A);
                        try {
                            if (o[i][2] = 1, 1 == (g = W(a, A + 4, T - 3, [], t, _, null, 0))[0]) {
                                return g;
                            }
                        } catch (b) {
                            if (o[i] && o[i][1] && 1 == (g = W(a, o[i][1][0], o[i][1][1], [], t, _, b, 0))[0]) {
                                return g;
                            }
                        } finally {
                            if (o[i] && o[i][0] && 1 == (g = W(a, o[i][0][0], o[i][0][1], [], t, _, null, 0))[0]) {
                                return g;
                            }
                            o[i] = 0, i--;
                        }
                        A += 2 * T - 2;
                    } else {
                        P < 7 ? (T = l(a, A), A += 2, O[S -= T] = 0 === T ? new O[S]() : d(O[S], f(O.slice(S + 1, S + T + 1)))) : P < 9 && (g = O[S--],
                        O[S] = O[S] & g);
                    }
                } else if (P < 3) {
                    P = 3 & E;
                    if (E >>= 2, P > 2) {
                        (P = E) > 7 ? (g = O[S--], O[S] = O[S] | g) : P > 5 ? (T = l(a, A), A += 2, O[++S] = t["$" + T]) : P > 3 && (T = u(a, A),
                        o[i][0] && !o[i][2] ? o[i][1] = [ A + 4, T - 3 ] : o[i++] = [ 0, [ A + 4, T - 3 ], 0 ],
                        A += 2 * T - 2);
                    } else if (P > 1) {
                        if ((P = E) > 13) {
                            O[++S] = !1;
                        } else if (P > 6) {
                            g = O[S--], O[S] = O[S] instanceof g;
                        } else if (P > 4) {
                            g = O[S--], O[S] = O[S] % g;
                        } else if (P > 2) {
                            if (O[S--]) {
                                A += 4;
                            } else {
                                if ((T = u(a, A)) < 0) {
                                    y = 1, q(a, b, 2 * c), A += 2 * T - 2;
                                    break;
                                }
                                A += 2 * T - 2;
                            }
                        } else if (P > 0) {
                            for (T = v(a, A), g = "", M = r.q[T][0]; M < r.q[T][1]; M++) {
                                g += String.fromCharCode(n ^ r.p[M]);
                            }
                            O[++S] = g, A += 4;
                        }
                    } else {
                        P > 0 ? (P = E) < 1 ? O[++S] = h : P < 3 ? (g = O[S--], O[S] = O[S] + g) : P < 5 && (g = O[S--],
                        O[S] = O[S] == g) : (P = E) > 13 ? (O[++S] = u(a, A), A += 4) : P > 11 ? (g = O[S--],
                        O[S] = O[S] >> g) : P > 9 ? (T = l(a, A), A += 2, g = O[S--], t[T] = g) : P > 7 ? (T = v(a, A),
                        A += 4, w = S + 1, O[S -= T - 1] = T ? O.slice(S, w) : []) : P > 0 && (g = O[S--],
                        O[S] = O[S] > g);
                    }
                } else {
                    P = 3 & E;
                    if (E >>= 2, P > 2) {
                        (P = E) < 2 ? (g = O[S--], O[S] = O[S] < g) : P < 9 ? (T = l(a, A), A += 2, O[S] = O[S][T]) : P < 11 ? O[++S] = !0 : P < 13 ? (g = O[S--],
                        O[S] = O[S] >>> g) : P < 15 && (O[++S] = s(a, A), A += 8);
                    } else if (P > 1) {
                        (P = E) < 6 || (P < 8 ? g = O[S--] : P < 10 ? (g = O[S--], O[S] = O[S] ^ g) : P < 12 && (T = u(a, A),
                        o[++i] = [ [ A + 4, T - 3 ], 0, 0 ], A += 2 * T - 2));
                    } else if (P > 0) {
                        (P = E) < 5 ? (T = l(a, A), A += 2, g = t[T], O[++S] = g) : P < 7 ? O[S] = ++O[S] : P < 9 && (g = O[S--],
                        O[S] = O[S] in g);
                    } else if ((P = E) > 13) {
                        g = O[S], O[S] = O[S - 1], O[S - 1] = g;
                    } else if (P > 4) {
                        g = O[S--], O[S] = O[S] === g;
                    } else if (P > 2) {
                        g = O[S--], O[S] = O[S] - g;
                    } else if (P > 0) {
                        for (T = v(a, A), P = "", M = r.q[T][0]; M < r.q[T][1]; M++) {
                            P += String.fromCharCode(n ^ r.p[M]);
                        }
                        P = +P, A += 4, O[++S] = P;
                    }
                }
            }
        }
        if (y) {
            for (;A < C; ) {
                j = V[A], A += 2, P = 3 & (E = 13 * j % 241);
                if (E >>= 2, P > 2) {
                    P = 3 & E;
                    if (E >>= 2, P > 2) {
                        (P = E) > 13 ? (O[++S] = F[A], A += 8) : P > 11 ? (g = O[S--], O[S] = O[S] >>> g) : P > 9 ? O[++S] = !0 : P > 7 ? (T = F[A],
                        A += 2, O[S] = O[S][T]) : P > 0 && (g = O[S--], O[S] = O[S] < g);
                    } else if (P > 1) {
                        (P = E) < 6 || (P < 8 ? g = O[S--] : P < 10 ? (g = O[S--], O[S] = O[S] ^ g) : P < 12 && (T = F[A],
                        o[++i] = [ [ A + 4, T - 3 ], 0, 0 ], A += 2 * T - 2));
                    } else if (P > 0) {
                        (P = E) < 5 ? (T = F[A], A += 2, g = t[T], O[++S] = g) : P < 7 ? O[S] = ++O[S] : P < 9 && (g = O[S--],
                        O[S] = O[S] in g);
                    } else if ((P = E) > 13) {
                        g = O[S], O[S] = O[S - 1], O[S - 1] = g;
                    } else if (P > 4) {
                        g = O[S--], O[S] = O[S] === g;
                    } else if (P > 2) {
                        g = O[S--], O[S] = O[S] - g;
                    } else if (P > 0) {
                        for (T = F[A], P = "", M = r.q[T][0]; M < r.q[T][1]; M++) {
                            P += String.fromCharCode(n ^ r.p[M]);
                        }
                        P = +P, A += 4, O[++S] = P;
                    }
                } else if (P > 1) {
                    P = 3 & E;
                    if (E >>= 2, P > 2) {
                        (P = E) < 5 ? (T = F[A], o[i][0] && !o[i][2] ? o[i][1] = [ A + 4, T - 3 ] : o[i++] = [ 0, [ A + 4, T - 3 ], 0 ],
                        A += 2 * T - 2) : P < 7 ? (T = F[A], A += 2, O[++S] = t["$" + T]) : P < 9 && (g = O[S--],
                        O[S] = O[S] | g);
                    } else if (P > 1) {
                        if ((P = E) < 2) {
                            for (T = F[A], g = "", M = r.q[T][0]; M < r.q[T][1]; M++) {
                                g += String.fromCharCode(n ^ r.p[M]);
                            }
                            O[++S] = g, A += 4;
                        } else {
                            P < 4 ? O[S--] ? A += 4 : A += 2 * (T = F[A]) - 2 : P < 6 ? (g = O[S--], O[S] = O[S] % g) : P < 8 ? (g = O[S--],
                            O[S] = O[S] instanceof g) : P < 15 && (O[++S] = !1);
                        }
                    } else {
                        P > 0 ? (P = E) < 1 ? O[++S] = h : P < 3 ? (g = O[S--], O[S] = O[S] + g) : P < 5 && (g = O[S--],
                        O[S] = O[S] == g) : (P = E) < 2 ? (g = O[S--], O[S] = O[S] > g) : P < 9 ? (T = F[A],
                        A += 4, w = S + 1, O[S -= T - 1] = T ? O.slice(S, w) : []) : P < 11 ? (T = F[A],
                        A += 2, g = O[S--], t[T] = g) : P < 13 ? (g = O[S--], O[S] = O[S] >> g) : P < 15 && (O[++S] = F[A],
                        A += 4);
                    }
                } else if (P > 0) {
                    P = 3 & E;
                    if (E >>= 2, P < 1) {
                        if ((P = E) < 5) {
                            T = F[A];
                            try {
                                if (o[i][2] = 1, 1 == (g = W(a, A + 4, T - 3, [], t, _, null, 0))[0]) {
                                    return g;
                                }
                            } catch (b) {
                                if (o[i] && o[i][1] && 1 == (g = W(a, o[i][1][0], o[i][1][1], [], t, _, b, 0))[0]) {
                                    return g;
                                }
                            } finally {
                                if (o[i] && o[i][0] && 1 == (g = W(a, o[i][0][0], o[i][0][1], [], t, _, null, 0))[0]) {
                                    return g;
                                }
                                o[i] = 0, i--;
                            }
                            A += 2 * T - 2;
                        } else {
                            P < 7 ? (T = F[A], A += 2, O[S -= T] = 0 === T ? new O[S]() : d(O[S], f(O.slice(S + 1, S + T + 1)))) : P < 9 && (g = O[S--],
                            O[S] = O[S] & g);
                        }
                    } else if (P < 2) {
                        if ((P = E) < 8) {
                            w = O[S--], g = delete O[S--][w];
                        } else if (P < 10) {
                            for (T = F[A], P = "", M = r.q[T][0]; M < r.q[T][1]; M++) {
                                P += String.fromCharCode(n ^ r.p[M]);
                            }
                            A += 4, O[S] = O[S][P];
                        } else {
                            P < 12 ? (g = O[S--], O[S] = O[S] << g) : P < 14 && (O[++S] = F[A], A += 2);
                        }
                    } else {
                        P < 3 ? (P = E) < 2 ? O[++S] = g : P < 11 ? (g = O[S -= 2][O[S + 1]] = O[S + 2],
                        S--) : P < 13 && (g = O[S], O[++S] = g) : (P = E) > 12 ? O[++S] = _ : P > 5 ? (g = O[S--],
                        O[S] = O[S] !== g) : P > 3 ? (g = O[S--], O[S] = O[S] / g) : P > 1 ? A += 2 * (T = F[A]) - 2 : P > -1 && (O[S] = !O[S]);
                    }
                } else {
                    P = 3 & E;
                    if (E >>= 2, P < 1) {
                        if ((P = E) < 1) {
                            return [ 1, O[S--] ];
                        }
                        if (P < 5) {
                            g = O[S--], O[S] = O[S] * g;
                        } else if (P < 7) {
                            g = O[S--], O[S] = O[S] != g;
                        } else if (P < 14) {
                            w = O[S--], m = O[S--], (P = O[S--]).x === W ? P.y >= 1 ? O[++S] = $(a, P.c, P.l, w, P.z, m, null, 1) : (O[++S] = $(a, P.c, P.l, w, P.z, m, null, 0),
                            P.y++) : O[++S] = P.apply(m, w);
                        } else if (P < 16) {
                            var k;
                            T = F[A], (k = function b() {
                                var c = arguments;
                                return b.y > 0 ? $(a, b.c, b.l, c, b.z, this, null, 0) : (b.y++, $(a, b.c, b.l, c, b.z, this, null, 0));
                            }).c = A + 4, k.l = T - 2, k.x = W, k.y = 0, k.z = t, O[S] = k, A += 2 * T - 2;
                        }
                    } else if (P < 2) {
                        (P = E) > 8 ? (g = O[S--], O[S] = typeof g) : P > 4 ? O[S -= 1] = O[S][O[S + 1]] : P > 2 && (w = O[S--],
                        (P = O[S]).x === W ? P.y >= 1 ? O[S] = $(a, P.c, P.l, [ w ], P.z, m, null, 1) : (O[S] = $(a, P.c, P.l, [ w ], P.z, m, null, 0),
                        P.y++) : O[S] = P(w));
                    } else if (P < 3) {
                        if ((P = E) < 9) {
                            for (g = O[S--], T = F[A], P = "", M = r.q[T][0]; M < r.q[T][1]; M++) {
                                P += String.fromCharCode(n ^ r.p[M]);
                            }
                            A += 4, O[S--][P] = g;
                        } else if (P < 13) {
                            throw O[S--];
                        }
                    } else {
                        (P = E) > 10 ? O[++S] = void 0 : P > 1 ? (g = O[S--], O[S] = O[S] >= g) : P > -1 && (O[++S] = null);
                    }
                }
            }
        }
        return [ 0, null ];
    }
    function $(a, b, c, e, d, t, f, r) {
        var n, o;
        null == t && (t = this), d && !d.d && (d.d = 0, d.$0 = d, d[1] = {});
        var i = {}, _ = i.d = d ? d.d + 1 : 0;
        for (i["$" + _] = i, o = 0; o < _; o++) {
            i[n = "$" + o] = d[n];
        }
        for (o = 0, _ = i.length = e.length; o < _; o++) {
            i[o] = e[o];
        }
        return r && !V[b] && q(a, b, 2 * c), V[b] ? W(a, b, c, 0, i, t, null, 1)[1] : W(a, b, c, 0, i, t, null, 0)[1];
    }
}

function _0x38c772(a, b) {
    return jsvmp("484e4f4a403f524300300d2ca1c1810d0da5c7b0000000000000048c1b0002001e1d00121b00131e00061a001d001f1b000b070200200200210d1b000b070200220200230d1b000b070200240200250d1b001b000b071b000b05191d00031b000200001d00261b0048001d00271b000b041e00281b000b0b4803283b1700f11b001b000b04221e0029241b001e0027222d1b00241d00270a0001104900ff2f4810331b000b04221e0029241b001e0027222d1b00241d00270a0001104900ff2f480833301b000b04221e0029241b001e0027222d1b00241d00270a0001104900ff2f301d002a1b00220b091b000b08221e002b241b000b0a4a00fc00002f4812340a000110281d00261b00220b091b000b08221e002b241b000b0a4a0003f0002f480c340a000110281d00261b00220b091b000b08221e002b241b000b0a490fc02f4806340a000110281d00261b00220b091b000b08221e002b241b000b0a483f2f0a000110281d002616ff031b000b041e00281b000b0b294800391700e01b001b000b04221e0029241b001e0027222d1b00241d00270a0001104900ff2f4810331b000b041e00281b000b0b3917001e1b000b04221e0029241b000b0b0a0001104900ff2f4808331600054800301d002a1b00220b091b000b08221e002b241b000b0a4a00fc00002f4812340a000110281d00261b00220b091b000b08221e002b241b000b0a4a0003f0002f480c340a000110281d00261b00220b091b000b041e00281b000b0b3917001e1b000b08221e002b241b000b0a490fc02f4806340a0001101600071b000b06281d00261b00220b091b000b06281d00261b000b090000002c000160203333333333333333333333333333333333333333333333333333333333333333016d0e3130333c3b3005273a253027212c023c31061a373f3036210332302108313037203232302707303b23363a313007363a3b263a393007333c27303720320a3a20213027023c31213d0a3c3b3b3027023c31213d0b3a202130271d303c323d210b3c3b3b30271d303c323d2109202630271432303b210b213a193a223027163426300163073c3b31302d1a33083039303621273a3b09203b3130333c3b30310925273a213a212c253008213a0621273c3b3204363439390725273a36302626100e3a373f3036217525273a3630262608063a373f30362105213c213930043b3a31300168016202266541141716111013121d1c1f1e19181b1a05040706010003020d0c0f343736313033323d3c3f3e39383b3a25242726212023222d2c2f65646766616063626d6c7e7a6802266441113e3125323d610f1e2604176d657a1833232266630d1c640767607e02001439103c621b19373a240c011a05202f38133f1f3b272c2d6c1d03123634062116306802266741113e3125323d610f1e2604176d657a1833232266630d1c640767607802001439103c621b19373a240c011a05202f38133f1f3b272c2d6c1d031236340621163068016c0264640639303b32213d0a363d3427163a3130142102646506363d34271421", [, , , _0x38c772, a, b]);
}
data = 'aweme_id=7304606061573573923&item_type=0&type=0'
url = 'device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2056&screen_height=1329&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=150&webid=7304128530371053090&msToken=1kGmD3bUceFReRz7FABJgZI1zE4D33lXZC5t1gMwgMkM-M1ram8QEuv713eezmTHXJmz6ByJSyPHpYUxndKAXLzove-dQ1vlkqwDI95ZebAP-KWseauYGKtEBVy1-zWO'

uas = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
console.log(getXBogus(url, data, uas));