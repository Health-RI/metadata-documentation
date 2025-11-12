<style>
/* Simple, small table with dark mode */
table {
  border-collapse: collapse;
  font-family: sans-serif;
  font-size: 11px;       /* one point larger */
  line-height: 1.2;
}

th, td {
  border: 1px solid #ccc;
  padding: 2px 4px;      /* compact spacing */
  text-align: left;
  vertical-align: top;
}

th {
  background: #d9edf7;   /* softer blue header for contrast */
  font-weight: bold;
}

tr:nth-child(even) {
  background: #f9f9f9;
}

tr:hover {
  background: #e6f2ff;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  table {
    background-color: #111;
    color: #eee;
  }
  th {
    background-color: #004466; /* deep blue header in dark mode */
    color: #fff;
  }
  td {
    border: 1px solid #444;
  }
  tr:nth-child(even) {
    background-color: #1a1a1a;
  }
  tr:hover {
    background-color: #333366;
  }
}

</style>
