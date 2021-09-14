library ieee;
use ieee.std_logic_1164.all;

entity exercicio03 is
port( E: in std_logic_vector(1 downto 0);
      En: in std_logic; 
      S: out std_logic_vector(7 downto 0) );
end exercicio03;

architecture mydec of exercicio03 is
begin
  S <= "00000000" when En = '0' else
      "10000001" when E = "11" else
      "01000010" when E = "10" else
      "00100100" when E = "01" else
      "00011000";
end mydec;