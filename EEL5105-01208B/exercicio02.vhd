library ieee;
use ieee.std_logic_1164.all;

entity exercicio02 is
port( X: in std_logic_vector(7 downto 0);
      KEY: in std_logic; 
      S1, S2, S3: out std_logic_vector(6 downto 0) );
end exercicio02;

architecture rtl of exercicio02 is
  signal C,D: std_logic_vector(7 downto 0);
  signal bcd, bcd2: std_logic_vector(11 downto 0);
  signal AS1,AS2,AS3,AS4,AS5,AS6: std_logic_vector(6 downto 0);

  component soma8 is
  port( A,B: in std_logic_vector(7 downto 0);
        S: out std_logic_vector(7 downto 0)
      );
  end component;

  component binbcd is
  port( bin_in: in std_logic_vector(7 downto 0);
        bcd_out: out std_logic_vector(11 downto 0)
      );
  end component;

  component bcd7seg is
  port( bcd_in:  in std_logic_vector(3 downto 0);
        out_7seg:  out std_logic_vector(6 downto 0)
      );
  end component;

begin
  SO1: soma8 port map (
    A => X, 
    B => X,
    S => C
  );

  SO2: soma8 port map (
    A => C,
    B => "00100000",
    S => D
  );

  BI1: binbcd port map (
    bin_in => D,
    bcd_out => bcd
  );

  BI2: binbcd port map (
    bin_in => X,
    bcd_out => bcd2
  );

  SEG1: bcd7seg port map (
    bcd_in => bcd(3 downto 0),
    out_7seg => AS1
  );

  SEG2: bcd7seg port map (
    bcd_in => bcd(7 downto 4),
    out_7seg => AS2
  );

  SEG3: bcd7seg port map (
    bcd_in => bcd(11 downto 8),
    out_7seg => AS3
  );

  SEG4: bcd7seg port map (
    bcd_in => bcd2(3 downto 0),
    out_7seg => AS4
  );

  SEG5: bcd7seg port map (
    bcd_in => bcd2(7 downto 4),
    out_7seg => AS5
  );

  SEG6: bcd7seg port map (
    bcd_in => bcd2(7 downto 4),
    out_7seg => AS6
  );

  S1 <= AS1 when KEY = '0' else AS4;
  S2 <= AS2 when KEY = '0' else AS5;
  S3 <= AS3 when KEY = '0' else AS6;

end rtl;