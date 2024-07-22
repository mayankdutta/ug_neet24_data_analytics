Show students percentage having marks b/w 550 & 600, 600+.
```sql
SELECT
  COUNT(info.serialNumber) AS totalStudents,
  SUM(CASE WHEN info.Marks BETWEEN 600 AND 720 THEN 1 ELSE 0 END) AS Marks600to720,
  SUM(CASE WHEN info.Marks BETWEEN 550 AND 600 THEN 1 ELSE 0 END) AS Marks550to600,
  ROUND(SUM(CASE WHEN info.Marks BETWEEN 600 AND 720 THEN 1 ELSE 0 END) / COUNT(info.serialNumber) * 100, 2) AS PercAbove600,
  ROUND(SUM(CASE WHEN info.Marks BETWEEN 550 AND 600 THEN 1 ELSE 0 END) / COUNT(info.serialNumber) * 100, 2) AS Perc550to600,

  info.centerName,
  info.centerCity,
  info.centerState
FROM
  `centering-sweep-430016-c4.neet.info` AS info
GROUP BY
  6,
  7,
  8
ORDER BY
  PercAbove600 DESC;
```

Students in particular center of a city, scoring 650+ 
```sql
WITH
  CenterStats AS (
  SELECT
    centerCity,
    centerName,
    COUNT(*) AS totalStudents,
    SUM(CASE
        WHEN Marks BETWEEN 650 AND 720 THEN 1
        ELSE 0
    END
      ) AS studentsFrom650to720
  FROM
    `centering-sweep-430016-c4.neet.info`
  WHERE
    centerCity IN (
      -- 'REWARI'
      'HISSAR'
      -- 'SIRSA'
      )
  GROUP BY
    centerCity,
    centerName )
SELECT
  CenterCity,
  centerName,
  totalStudents,
  studentsFrom650to720,
  ROUND((studentsFrom650to720 * 100.0 / totalStudents), 2) AS percentage650to720,
FROM
  `CenterStats`
ORDER BY
  percentage650to720 DESC ;
```


Student with rank 
```sql
SELECT 
    centerNumber,
    serialNumber,
    Marks,
    centerName,
    centerCity,
    centerState,
    RANK() OVER (ORDER BY Marks DESC) AS Rank
FROM `centering-sweep-430016-c4.neet.info`
    
ORDER BY 
    Marks DESC;
```
