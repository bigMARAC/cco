library IEEE;
use IEEE.Std_Logic_1164.all;

entity exercicio01 is
port (SW: in std_logic_vector(3 downto 0);
        LEDR: out std_logic_vector(3 downto 0)
        );
end exercicio01;

architecture circuito_logico of exercicio01 is
  signal A, B, C, D, W, X, Y, Z: std_logic;
begin 

  A <= SW(3);
  B <= SW(2);
  C <= SW(1);
  D <= SW(0);
  
  LEDR(3) <= W;
  LEDR(2) <= X;
  LEDR(1) <= Y;
  LEDR(0) <= Z;
  
  W <= ((not A) and C) or ((not A) and B) or (A and (not B) and (not C)) or (C and (not D));
  X <= ((not A) and (not B) and C) or ((not A) and B and (not C)) or ((not A) and (not C) and D);
  Y <= (B and C and (not D)) or (A and (not C) and (not D)) or (A and (not D));
  Z <= (not A) or ((not B) and (not C)) or (C and (not D));
  
end circuito_logico;