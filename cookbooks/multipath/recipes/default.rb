vim_base_pkgs = value_for_platform(
    ["ubuntu", "redhat", "centos"] => { "default" => ["multipath-tools"] },
    "default" => ["multipath-tools"]
)

vim_base_pkgs.each do |vim_base_pkg|
      package vim_base_pkg
end

