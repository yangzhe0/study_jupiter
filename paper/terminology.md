# 中英文术语对照表

> 维护原则：中文初稿和后续英文稿均以本表为准。未核验的中文名词先标记“待核验”，后续优先使用中国天文学名词数据库（NADC 天文学名词）确认。

| 中文术语 | 英文术语 | 缩写/符号 | 推荐用法 | 状态/来源 |
|---|---|---|---|---|
| 木星卫星 | Jovian satellites |  | 指木星天然卫星整体；避免混用 Jupiter moons 作为正式术语 | 待核验 |
| J1-J18 木星卫星 | J1-J18 Jovian satellites | J1-J18 | 研究对象范围 | 待核验 |
| 天体测量 | astrometry |  | 地基天体测量资料 | 待核验 |
| 地基观测 | ground-based observations |  | 与 spacecraft observations 区分 | 待核验 |
| 观测星表 | observational catalog |  | 本文核心数据产品；避免在同一语境混用 observation table / data catalog | 待核验 |
| 观测资料 | observational data |  | 泛指原始或整理后的观测数据 | 待核验 |
| 观测记录 | observation record |  | 星表中的一行或一条观测记录，需与 observed coordinates 区分 | 自定义，待定 |
| 观测坐标 | observed coordinates |  | 一条记录可能含两个坐标分量 | 参考 Yuan et al. 2021 |
| 观测夜 | observation night |  | 用于统计时间覆盖 | 待核验 |
| 时标 | timescale |  | 统一到 TT | 待核验 |
| 地球时 | Terrestrial Time | TT | 首次出现写“地球时（TT）” | 待核验 |
| 协调世界时 | Coordinated Universal Time | UTC | 原始时标之一 | 待核验 |
| 世界时 | Universal Time | UT | 原始时标之一 | 待核验 |
| 历书时 | Ephemeris Time | ET | 原始时标之一 | 待核验 |
| 地球动力学时 | Terrestrial Dynamical Time | TDT | 与 TT 历史关系需说明 | 待核验 |
| 参考系 | reference system |  | 统一到 ICRS | 待核验 |
| 国际天球参考系 | International Celestial Reference System | ICRS | 首次出现写全称 | 待核验 |
| 赤经 | right ascension | RA, α | 公式中用 α | 待核验 |
| 赤纬 | declination | Dec, δ | 公式中用 δ | 待核验 |
| 位置角 | position angle | PA, p | 相对观测量 | 待核验 |
| 角距 | angular separation | s | 相对观测量 | 待核验 |
| 切平面坐标 | tangential coordinates |  | 需核验中文标准译名 | 待核验 |
| 差分坐标 | differential coordinates |  | 需核验中文标准译名 | 待核验 |
| 视差 | parallax |  | 使用 NADC 天文学名词确认 | 待核验，用户示例 |
| 自行 | proper motion |  | Gaia 星表参数 | 待核验 |
| 岁差 | precession |  | 参考系转换项 | 待核验 |
| 章动 | nutation |  | 参考系转换项 | 待核验 |
| 光行时 | light-time |  | O-C 计算中可能涉及 | 待核验 |
| 像差 | aberration |  | O-C 计算中可能涉及 | 待核验 |
| 大气折射 | atmospheric refraction |  | 观测改正项 | 待核验 |
| 相位效应 | phase effect |  | 观测改正项 | 待核验 |
| 星历 | ephemeris |  | 单数 ephemeris，复数 ephemerides | 待核验 |
| 行星历 | planetary ephemeris |  | DE441 | 待核验 |
| 卫星星历 | satellite ephemeris |  | jup347 | 待核验 |
| 观测量与理论量之差 | observed minus computed residuals | O-C residuals | 中文正文可写 O-C 残差 | 待核验 |
| 星表系统误差 | star-catalog systematic errors |  | 可简称星表偏差，但全文需统一 | 待核验 |
| 星表偏差改正 | star-catalog bias correction |  | 基于 Gaia DR3 | 待核验 |
| 参考星表 | reference star catalog |  | Gaia DR3 等 | 待核验 |
| 离群值 | outlier |  | 异常记录标记 | 待核验 |
| 质量标记 | quality flag |  | 输出星表字段 | 自定义，待定 |
| 原始字段 | original fields |  | 星表字段分组 | 自定义 |
| 标准化字段 | standardized fields |  | 星表字段分组 | 自定义 |
| 数据溯源 | provenance |  | 记录数据库、原始文件、文献来源和处理历史 | 自定义，待核验 |
| 比较天体 | comparison body |  | 相对观测中作为参考的天体 | 待核验，需查 NADC |
| 参考天体 | reference body |  | 与 comparison body 区分待定；用于相对观测转换 | 待核验，需查 NADC |
| 绝对坐标 | absolute coordinates | ABS | 观测量类型枚举；赤经、赤纬 | 参考 Yuan et al. 2021，中文待核验 |
| 位置角和角距 | position angle and separation | PAS | 观测量类型枚举；相对位置 | 参考 Yuan et al. 2021，中文待核验 |
| 观测量类型 | observable type | obs | 星表字段；记录 ABS/PAS/TAN/DIF/DRD 等 | 自定义，待定 |
| 星表偏差改正量 | star-catalog bias correction | catBias | 输出字段；相对于 Gaia DR3 的赤经、赤纬方向改正量 | 自定义，待定 |
| 去偏前残差 | residuals before catalog-bias correction | rsdIcrsB | 输出字段候选名 | 自定义，待定 |
| 去偏后残差 | residuals after catalog-bias correction | rsdIcrsA | 输出字段候选名 | 自定义，待定 |
| 修正儒略日 | Modified Julian Day | MJD | 输出时刻候选格式 MJD_TT | 待核验 |
| 数据边界 | data boundary |  | 说明纳入和未纳入的数据范围 | 自定义 |

## 卫星名称表（待核验）

| 编号 | 英文名称 | 中文名称 | 备注 |
|---|---|---|---|
| J1 | Io | 伊娥 | 待核验 |
| J2 | Europa | 欧罗巴 | 待核验 |
| J3 | Ganymede | 甘尼米德 | 待核验 |
| J4 | Callisto | 卡利斯托 | 待核验 |
| J5 | Amalthea | 阿玛尔忒亚 | 待核验 |
| J6 | Himalia | 希玛利亚 | 待核验 |
| J7 | Elara | 厄拉拉 | 待核验 |
| J8 | Pasiphae | 帕西法厄 | 待核验 |
| J9 | Sinope | 锡诺普 | 待核验 |
| J10 | Lysithea | 利西忒亚 | 待核验 |
| J11 | Carme | 卡尔墨 | 待核验 |
| J12 | Ananke | 阿南刻 | 待核验 |
| J13 | Leda | 勒达 | 待核验 |
| J14 | Thebe | 忒拜 | 待核验 |
| J15 | Adrastea | 阿德剌斯忒亚 | 待核验 |
| J16 | Metis | 墨提斯 | 待核验 |
| J17 | Callirrhoe | 卡利罗厄 | 待核验 |
| J18 | Themisto | 忒弥斯托 | 待核验 |
