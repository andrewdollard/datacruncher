Database Project

implementing B-Tree index:
  implement binary format for page-structured heap file
  load CSV into a page-structured heap file
  created sorted version of heap file (out-of-core sort)
  implement binary format for index nodes
  scan sorted heap file and build index

options for cleanly reading sorted page sections in intermediary files:
  * make all columns fixed size, so that all pages contain precisely the same number of records
  * keep a data structure between each iteration, with pointers to each section
  * include a waypoint record that points to the next sorted section


