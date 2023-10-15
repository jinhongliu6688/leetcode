- Learn from https://leetcode.com/problems/rotate-image/solutions/18872/a-common-method-to-rotate-the-image/

- clockwise rotate: first reverse up to down, then swap the symmetry
  
  <img width="229" alt="image" src="https://github.com/jinhongliu6688/leetcode/assets/112588153/385dcd38-c9d6-4b40-aefa-7320154976e4">


- IMPORTANT: matrix = matrix[::-1] does not work, matrix.reverse() works
