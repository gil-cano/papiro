.. _performance:

===========
Performance
===========

.. topic:: Description

   This text will go to Plone's pages description field.

Prueba de desempeño
-------------------

Realizamos una prueba con `Apache HTTP server benchmarking tool (ab) <http://httpd.apache.org/docs/2.2/programs/ab.html>`_, realizando 25 peticioones, dos al mismo tiempo.

.. code-block:: shell

    $ ab -n 25 -c 2 [URL]

    Server Software:        Zope/(2.13.22,
    Server Hostname:        localhost
    Server Port:            0000

    Document Path:          /test
    Document Length:        92039 bytes

    Concurrency Level:      2
    Time taken for tests:   22.231 seconds
    Complete requests:      25
    Failed requests:        0
    Total transferred:      2310000 bytes
    HTML transferred:       2300975 bytes
    Requests per second:    1.12 [#/sec] (mean)
    Time per request:       1778.475 [ms] (mean)
    Time per request:       889.238 [ms] (mean, across all concurrent requests)
    Transfer rate:          101.47 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       0
    Processing:   233 1146 3057.7    466   15591
    Waiting:      233 1143 3058.4    465   15591
    Total:        234 1146 3057.8    467   15591

    Percentage of the requests served within a certain time (ms)
      50%    465
      66%    469
      75%    470
      80%    474
      90%    672
      95%   3114
      98%  15591
      99%  15591
     100%  15591 (longest request)


* `Plone Performance Troubleshooting <http://www.tandj.net/~simkintr/news/2014/plone-performance-troubleshooting-contextstate.actions>`_



